import os
import sys
import math
import time
import logging
import platform

from .Protocol import Protocol

SOH = b'\x01'
STX = b'\x02'
EOT = b'\x04'
ACK = b'\x06'
NAK = b'\x15'
CAN = b'\x18'
CRC = b'\x43'

USE_LENGTH_FIELD    = 0b100000
USE_DATE_FIELD      = 0b010000
USE_MODE_FIELD      = 0b001000
USE_SN_FIELD        = 0b000100
ALLOW_1K_PACKET     = 0b000010
ALLOW_YMODEM_G      = 0b000001

class Modem(Protocol):
    def __init__(self, reader, writer, mode='ymodem1k', program="rzsz"):
        self.logger = logging.getLogger('Modem')
        self.platform = sys.platform
        self.reader = reader
        self.writer = writer
        self.mode   = mode
        # handler = logging.FileHandler("log.txt")
        # handler.setLevel(logging.DEBUG)
        # self.logger.addHandler(handler)
        # self.logger.setLevel(level = logging.DEBUG)

        '''
        YMODEM Header Information and Features
        _____________________________________________________________
        | Program   | Length | Date | Mode | S/N | 1k-Blk | YMODEM-g |
        |___________|________|______|______|_____|________|__________|
        |Unix rz/sz | yes    | yes  | yes  | no  | yes    | sb only  |
        |___________|________|______|______|_____|________|__________|
        |VMS rb/sb  | yes    | no   | no   | no  | yes    | no       |
        |___________|________|______|______|_____|________|__________|
        |Pro-YAM    | yes    | yes  | no   | yes | yes    | yes      |
        |___________|________|______|______|_____|________|__________|
        |CP/M YAM   | no     | no   | no   | no  | yes    | no       |
        |___________|________|______|______|_____|________|__________|
        |KMD/IMP    | ?      | no   | no   | no  | yes    | no       |
        |___________|________|______|______|_____|________|__________|

        '''
        try:
            self.program_features = dict(
                rzsz    = USE_LENGTH_FIELD | USE_DATE_FIELD | USE_MODE_FIELD | ALLOW_1K_PACKET,
                rbsb    = USE_LENGTH_FIELD | ALLOW_1K_PACKET,
                pyam    = USE_LENGTH_FIELD | USE_DATE_FIELD | USE_SN_FIELD | ALLOW_1K_PACKET | ALLOW_YMODEM_G,
                cyam    = ALLOW_1K_PACKET,
                kimp    = ALLOW_1K_PACKET,
            )[program]
        except KeyError:
            raise ValueError("Invalid program specified: {}".format(program))
        
    def abort(self, count=2, timeout=60):
        for _ in range(count):
            self.writer.write(CAN, timeout)

    def send(self, file_paths, retry=10, timeout=10, callback=None):

        try:
            packet_size = dict(
                xmodem    = 128,
                xmodem1k  = 1024,
                ymodem    = 128,
                # Not all but most programs support 1k length
                ymodem1k  = (128, 1024)[(self.program_features & ALLOW_1K_PACKET) != 0],
            )[self.mode]
        except KeyError:
            raise ValueError("Invalid mode specified: {}.".format(self.mode))

        
        tasks = []

        for file_path in file_paths:
            tasks.append(
                {
                    "path": file_path,
                    "name": os.path.basename(file_path),
                    "length": os.path.getsize(file_path),
                    "mtime": os.path.getmtime(file_path)
                }
            )

        for task_index, task in enumerate(tasks):
            
            self.logger.debug("[Sender]: file %s, length %d bytes", task["name"], task["length"])
            try:
                stream = open(task["path"], 'rb')
            except IOError as e:
                self.logger.debug("[Sender]: Cannot open the file: %s.", task)
                return False

            if self.mode.startswith("ymodem"):

                '''
                Info packet
                '''
                crc_mode = 0
                cancel_count = 0
                error_count = 0
                while True:
                    # Blocking may occur here, the reader needs to have a timeout mechanism
                    char = self.reader.read(1, timeout)

                    if char == NAK:
                        crc_mode = 0
                        self.logger.debug("[Sender]: Received checksum request (NAK).")
                        break
                    elif char == CRC:
                        crc_mode = 1
                        self.logger.debug("[Sender]: Received CRC request (C/CRC).")
                        break
                    elif char == CAN:
                        if cancel_count == 0:
                            cancel_count += 1
                        else:
                            self.logger.debug("[Sender]: Cancel transfer (CAN).")
                            return False
                    else:
                        self.logger.debug("[Sender]: No valid data read.")

                    error_count += 1
                    if error_count > retry:
                        self.abort(timeout=timeout)
                        if stream:
                            stream.close()
                        self.logger.debug("[Sender]: Aborted, the number of errors has reached {}.".format(retry))
                        return False

                header = self._make_send_header(packet_size, 0)

                # Required field: Name
                data = task["name"].encode("utf-8")
                
                # Optional field: Length
                if self.program_features & USE_LENGTH_FIELD:
                    data += bytes(1)
                    data += str(task["length"]).encode("utf-8")

                
                # Optional field: Modification Date
                # oct() has different representations of octal numbers in different versions of Python:
                # Python 2+: 0123456
                # Python 3+: 0o123456
                if self.program_features & USE_DATE_FIELD:
                    mtime = oct(int(task["mtime"]))
                    if mtime.startswith("0o"):
                        data += (" " + mtime[2:]).encode("utf-8")
                    else:
                        data += (" " + mtime[1:]).encode("utf-8")

                # Optional field: Mode
                if self.program_features & USE_MODE_FIELD:
                    if self.platform == "linux":
                        data += (" " + oct(0x8000)).encode("utf-8")
                    else:
                        data += (" 0").encode("utf-8")

                # Optional field: Serial Number
                if self.program_features & USE_MODE_FIELD:
                    data += (" 0").encode("utf-8")

                data = data.ljust(packet_size, b"\x00")
                checksum = self._make_send_checksum(crc_mode, data)
                
                error_count = 0
                while True:
                    # Blocking may occur here, the writer needs to have a timeout mechanism
                    sdata = header + data + checksum
                    #self.writer.write(header + data + checksum)
                    self.writer.write(sdata)
                    self.logger.debug("[Sender]: Info packet sent")
                    self.logger.debug(sdata.hex(' '))

                    success = False
                    # Blocking may occur here, the reader needs to have a timeout mechanism
                    while True:
                        char = self.reader.read(1, timeout)
                        if char == ACK:
                            self.logger.debug("[Sender]: Received ack")
                            error_count = 0
                            success = True
                            break
                        elif char != None:
                            #print(char)
                            continue
                        else:
                            error_count += 1
                            self.logger.debug("[Sender]: No valid data read.")

                        if error_count > retry:
                            self.abort(timeout=timeout)
                            if stream:
                                stream.close()
                            self.logger.debug("[Sender]: Aborted, the number of errors has reached {}.".format(retry))
                            return False
                        
                    if success == True:
                        break
            '''
            Data packet
            '''
            crc_mode = 0
            cancel_count = 0
            error_count = 0
            while True:
                # Blocking may occur here, the reader needs to have a timeout mechanism
                char = self.reader.read(1, timeout)

                if char == NAK:
                    crc_mode = 0
                    self.logger.debug("[Sender]: Received checksum request (NAK).")
                    break
                elif char == CRC:
                    crc_mode = 1
                    self.logger.debug("[Sender]: Received CRC request (C/CRC).")
                    break
                elif char == CAN:
                    if cancel_count == 0:
                        cancel_count += 1
                    else:
                        self.logger.debug("[Sender]: Cancel transfer (CAN).")
                        return False
                else:
                    self.logger.debug("[Sender]: No valid data read.")

                error_count += 1
                if error_count > retry:
                    self.abort(timeout=timeout)
                    if stream:
                        stream.close()
                    self.logger.debug("[Sender]: Aborted, the number of errors has reached {}.".format(retry))
                    return False

            sequence = 1
            total_packet_count = math.ceil(task["length"] / packet_size)
            success_packet_count = 0
            error_packet_count = 0
            while True:
                try:
                    data = stream.read(packet_size)
                except Exception as e:
                    stream.close()
                    self.logger.debug("[Sender]: Failed to read file.")
                    return False

                if not data:
                    self.logger.debug("[Sender]: Reached EOF")
                    break

                header = self._make_send_header(packet_size, sequence)
                # fill with 1AH(^z)
                data = data.ljust(packet_size, b"\x1a")
                checksum = self._make_send_checksum(crc_mode, data)

                while True:
                    # Blocking may occur here, the writer needs to have a timeout mechanism
                    last_time = time.perf_counter()
                    sdata = header + data + checksum
                    self.writer.write(sdata)
                    #print(sdata.hex(' '))
                    cost = time.perf_counter() - last_time
                    self.logger.debug("[Sender]: Packet %d sent, %d bytes cost %.03f s.", sequence, len(sdata), cost)
                    self.logger.debug(sdata.hex(' '))

                    # Blocking may occur here, the reader needs to have a timeout mechanism
                    last_time = time.perf_counter()
                    char = self.reader.read(1, timeout)
                    cost = time.perf_counter() - last_time

                    if char == ACK:
                        success_packet_count += 1

                        self.logger.debug("[Sender]: Received ack cost %.03f s.", cost)
                        if callable(callback):
                            callback(task_index, task["name"], total_packet_count, success_packet_count, error_packet_count)

                        error_packet_count = 0
                        break
                    else:
                        error_packet_count += 1
                        self.logger.debug("[Sender]: Ready to resend packet %d.", sequence)

                        if callable(callback):
                            callback(task_index, task["name"], total_packet_count, success_packet_count, error_packet_count)

                        if error_packet_count > retry:
                            self.abort(timeout=timeout)
                            if stream:
                                stream.close()
                            self.logger.debug("[Sender]: Aborted, the number of errors has reached {}.".format(retry))
                            return False

                sequence = (sequence + 1) % 0x100

            self.logger.debug("[Sender]: %d of %d - %s completed.", task_index+1, len(tasks), task["name"])

            '''
            EOT 
            '''
            self.writer.write(EOT)
            self.logger.debug("[Sender]: EOT sent.")

            char = self.reader.read(1, timeout)
            if char != ACK:
                self.writer.write(EOT)
                self.logger.debug("[Sender]: EOT resent.")

                while True:
                    char = self.reader.read(1, timeout)
                    if char == ACK:
                        break
                    else:
                        error_count += 1
                        self.logger.debug("[Sender]: No valid data read.")

                    if error_count > retry:
                        self.abort(timeout=timeout)
                        if stream:
                            stream.close()
                        self.logger.debug("[Sender]: Aborted, the number of errors has reached {}.".format(retry))
                        return False

        if stream:
            stream.close()

        '''
        batch end packet
        '''
        header = self._make_send_header(packet_size, 0)
        data = bytearray().ljust(packet_size, b"\x00")
        checksum = self._make_send_checksum(crc_mode, data)
        sdata = header + data + checksum
        self.writer.write(sdata)
        self.logger.debug("[Sender]: Batch end packet sent.")
        self.logger.debug(sdata.hex(' '))
        char = self.reader.read(1, timeout)
        if char != ACK:
            self.logger.debug("[Sender]: No valid data read.")
        else:
            self.logger.debug("[Sender]: Received ack")

        return True


    def _make_send_header(self, packet_size, sequence):
        assert packet_size in (128, 1024), packet_size
        _bytes = []
        if packet_size == 128:
            _bytes.append(ord(SOH))
        elif packet_size == 1024:
            _bytes.append(ord(STX))
        _bytes.extend([sequence, 0xff - sequence])
        return bytearray(_bytes)

    def _make_send_checksum(self, crc_mode, data):
        _bytes = []
        if crc_mode:
            crc = self.calc_crc(data)
            _bytes.extend([crc >> 8, crc & 0xff])
        else:
            crc = self.calc_checksum(data)
            _bytes.append(crc)
        return bytearray(_bytes)

    def recv(self, folder_path, crc_mode=1, retry=10, timeout=10, delay=1, callback=None):

        # task index
        task_index = -1

        while True:

            task = {
                "name": "",
                "total_length": 0,
                "received_length": 0,
                "mtime": 0,
                "mode": 0,
                "sn": 0
            }
            
            '''
            Parse info packet
            '''
            if self.mode.startswith("ymodem"):

                char = 0
                cancel_count = 0
                error_count = 0
                while True:
                    if error_count >= retry:
                        self.abort(timeout=timeout)
                        self.logger.debug("[Receiver]: Aborted, the number of errors has reached {}.".format(retry))
                        return False
                    elif crc_mode and error_count < (retry // 2):
                        if not self.writer.write(CRC):
                            time.sleep(delay)
                            error_count += 1
                            self.logger.debug("[Receiver]: Failed to write CRC, sleep for {}s.".format(delay))
                    else:
                        crc_mode = 0
                        if not self.writer.write(NAK):
                            time.sleep(delay)
                            error_count += 1
                            self.logger.debug("[Receiver]: Failed to write NAK, sleep for {}s".format(delay))

                    char = self.reader.read(1, timeout=3)
                    if char == SOH or char == STX:
                        break
                    elif char == CAN:
                        if cancel_count == 0:
                            cancel_count += 1
                        else:
                            self.logger.debug("[Receiver]: Cancel transfer (CAN).")
                            return False
                    else:
                        error_count += 1
                        self.logger.debug("[Receiver]: No valid data received.")

                packet_size = 128
                cancel_count = 0
                error_count = 0
                while True:
                    while True:
                        if char == SOH:
                            packet_size = 128
                            self.logger.debug("[Receiver]: Set 128 bytes as packet size.")
                            break
                        elif char == STX:
                            packet_size = 1024
                            self.logger.debug("[Receiver]: Set 1024 bytes as packet size.")
                            break
                        elif char == CAN:
                            if cancel_count == 0:
                                cancel_count += 1
                            else:
                                self.logger.debug("[Receiver]: Cancel transfer (CAN).")
                                return False
                        else:
                            error_count += 1
                            self.logger.debug("[Receiver]: No valid data received.")

                        if error_count > retry:
                            self.abort(timeout=timeout)
                            self.logger.debug("[Receiver]: Aborted, the number of errors has reached {}.".format(retry))
                            return False

                    error_count = 0
                    seq1 = self.reader.read(1, timeout)
                    if seq1:
                        seq1 = ord(seq1)
                        seq2 = self.reader.read(1, timeout)
                        if seq2:
                            seq2 = 0xff - ord(seq2)
                    else:
                        seq2 = None

                    if not (seq1 == seq2 == 0):
                        self.logger.debug("[Receiver]: Expected seq 0 but got (seq1 %r, seq2 %r).", seq1, seq2)
                        # skip this packet
                        self.reader.read(packet_size + 1 + crc_mode)
                        self.logger.debug("[Receiver]: Dropped the broken packet.")
                    else:
                        data = self.reader.read(packet_size + 1 + crc_mode, timeout)

                        if data and len(data) == (packet_size + 1 + crc_mode):
                            valid, data = self._verify_recv_checksum(crc_mode, data)

                            if valid:

                                file_name = bytes.decode(data.split(b"\x00")[0], "utf-8")
                                
                                # batch end packet received
                                if not file_name:
                                    self.logger.debug("[Receiver]: Received batch end packet.")
                                    self.writer.write(ACK)
                                    return True

                                # info packet received
                                else:
                                    self.logger.debug("[Receiver]: Received info packet.")

                                task_index += 1
                                task["name"] = file_name
                                self.logger.debug("[Receiver]: File - {}".format(task["name"]))

                                data = bytes.decode(data.split(b"\x00")[1], "utf-8")

                                if self.program_features & USE_LENGTH_FIELD:
                                    space_index = data.find(" ")
                                    task["total_length"] = int(data if space_index == -1 else data[:space_index])
                                    self.logger.debug("[Receiver]: Size - {} bytes".format(task["total_length"]))
                                    data = data[space_index + 1:]

                                if self.program_features & USE_DATE_FIELD:
                                    space_index = data.find(" ")
                                    task["mtime"] = int(data if space_index == -1 else data[:space_index], 8)
                                    self.logger.debug("[Receiver]: Mtime - {} seconds".format(task["mtime"]))
                                    data = data[space_index + 1:]

                                if self.program_features & USE_MODE_FIELD:
                                    space_index = data.find(" ")
                                    task["mode"] = int(data if space_index == -1 else data[:space_index])
                                    self.logger.debug("[Receiver]: Mode - {}".format(task["mode"]))
                                    data = data[space_index + 1:]

                                if self.program_features & USE_SN_FIELD:
                                    space_index = data.find(" ")
                                    task["sn"] = int(data if space_index == -1 else data[:space_index])
                                    self.logger.debug("[Receiver]: SN - {}".format(task["sn"]))

                                self.writer.write(ACK)
                                break

                            # broken packet
                            else:
                                pass
                        
                        # bad read
                        else:
                            pass

                    # Receive failed handler: ask for retransmission
                    while True:
                        if not self.reader.read(1, timeout=1):
                            break
                    self.writer.write(NAK)
                    self.logger.debug("[Receiver]: Requesting retransmission (NAK).")

                    char = self.reader.read(1, timeout)

            # create file in saving folder
            p = os.path.join(folder_path, task["name"])
            try:
                stream = open(p, "wb+")
            except IOError as e:
                self.logger.debug("[Receiver]: Cannot open the save path: %s.", p)
                return False

            '''
            Parse data packet
            '''
            char = 0
            cancel_count = 0
            error_count = 0
            while True:
                if error_count >= retry:
                    self.abort(timeout=timeout)
                    if stream:
                        stream.close()
                    self.logger.debug("[Receiver]: Aborted, the number of errors has reached {}.".format(retry))
                    return False
                elif crc_mode and error_count < (retry // 2):
                    if not self.writer.write(CRC):
                        self.logger.debug("[Receiver]: Failed to write CRC, sleep for {}s.".format(delay))
                        time.sleep(delay)
                        error_count += 1
                else:
                    crc_mode = 0
                    if not self.writer.write(NAK):
                        self.logger.debug("[Receiver]: Failed to write NAK, sleep for {}s.".format(delay))
                        time.sleep(delay)
                        error_count += 1

                char = self.reader.read(1, timeout=3)
                if char == SOH or char == STX:
                    break
                elif char == CAN:
                    if cancel_count == 0:
                        cancel_count += 1
                    else:
                        self.logger.debug("[Receiver]: Cancel transfer (CAN).")
                        return False
                else:
                    error_count += 1
                    self.logger.debug("[Receiver]: No valid data read.")
                    
            
            eot_received = False
            packet_size = 128
            sequence = 1
            cancel_count = 0
            error_count = 0
            success_packet_count = 0
            error_packet_count = 0
            while True:
                while True:
                    if char == SOH:
                        packet_size = 128
                        self.logger.debug("[Receiver]: Set 128 bytes as packet size.")
                        break
                    elif char == STX:
                        packet_size = 1024
                        self.logger.debug("[Receiver]: Set 1024 bytes as packet size.")
                        break
                    elif char == EOT:
                        self.writer.write(ACK)
                        eot_received = True
                        self.logger.debug("[Receiver]: %d - %s completed.", task_index+1, task["name"])
                        break
                    elif char == CAN:
                        if cancel_count == 0:
                            cancel_count += 1
                        else:
                            if stream:
                                stream.close()
                            self.logger.debug("[Receiver]: Cancel transfer (CAN) at data packet {} (seq {}).".format(success_packet_count, sequence))
                            return False           
                    else:
                        error_count += 1
                        self.logger.debug("[Receiver]: No valid data received.")

                    if error_count > retry:
                        self.abort(timeout=timeout)
                        if stream:
                            stream.close()
                        self.logger.debug("[Receiver]: Aborted, the number of errors has reached {}.".format(retry))
                        return False
                
                if eot_received:
                    break

                total_packet_count = math.ceil(task["total_length"] / packet_size)

                seq1 = self.reader.read(1, timeout)
                if seq1:
                    seq1 = ord(seq1)
                    seq2 = self.reader.read(1, timeout)
                    if seq2:
                        seq2 = 0xff - ord(seq2)
                else:
                    seq2 = None

                # Packet received in wrong number
                if not (seq1 == seq2 == sequence):
                    self.logger.debug("[Receiver]: Expected seq %d but got (seq1 %r, seq2 %r).", sequence, seq1, seq2)
                    # skip this packet
                    self.reader.read(packet_size + 1 + crc_mode)
                    self.logger.debug("[Receiver]: Dropped the broken packet.")
                
                # Packet received
                else:
                    data = self.reader.read(packet_size + 1 + crc_mode, timeout)

                    if data and len(data) == (packet_size + 1 + crc_mode):
                        valid, data = self._verify_recv_checksum(crc_mode, data)

                        # Write the original data to the target file
                        if valid:
                            success_packet_count += 1
                            self.logger.debug("[Receiver]: Received data packet %d.", sequence)

                            valid_length = packet_size

                            # The last package adjusts the valid data length according to the file length
                            remaining_length = task["total_length"] - task["received_length"]
                            if (remaining_length > 0):
                                valid_length = min(valid_length, remaining_length)
                            data = data[:valid_length]

                            task["received_length"] += len(data)

                            try:
                                stream.write(data)
                            except Exception as e:
                                stream.close()
                                self.logger.debug("[Receiver]: Failed to write data packet %d to file.", sequence)
                                return False

                            self.logger.debug("[Receiver]: Successfully write data packet %d to file.", sequence)

                            if callable(callback):
                                callback(task_index, task["name"], total_packet_count, success_packet_count, error_packet_count)

                            self.writer.write(ACK)

                            sequence = (sequence + 1) % 0x100
                            char = self.reader.read(1, timeout)
                            continue

                        # broken packet
                        else:
                            error_packet_count += 1
                            self.logger.debug("[Receiver]: Received broken data packet.")

                            if callable(callback):
                                callback(task_index, task["name"], total_packet_count, success_packet_count, error_packet_count)

                    # bad read
                    else:
                        pass

                # Receive failed handler: ask for retransmission
                while True:
                    if not self.reader.read(1, timeout=1):
                        break
                self.writer.write(NAK)
                self.logger.debug("[Receiver]: Requested retransmission (NAK).")

                char = self.reader.read(1, timeout)

            if stream:
                stream.close()

    def _verify_recv_checksum(self, crc_mode, data):
        if crc_mode:
            _checksum = bytearray(data[-2:])
            remote_sum = (_checksum[0] << 8) + _checksum[1]
            data = data[:-2]

            local_sum = self.calc_crc(data)
            valid = bool(remote_sum == local_sum)
            if not valid:
                self.logger.debug("[Receiver]: CRC verification failed. Sender: %04x, Receiver: %04x.", remote_sum, local_sum)
        else:
            _checksum = bytearray([data[-1]])
            remote_sum = _checksum[0]
            data = data[:-1]

            local_sum = self.calc_checksum(data)
            valid = remote_sum == local_sum
            if not valid:
                self.logger.debug("[Receiver]: CRC verification failed. Sender: %02x, Receiver: %02x.", remote_sum, local_sum)
        return valid, data

    def calc_checksum(self, data, checksum=0):
        if platform.python_version_tuple() >= ('3', '0', '0'):
            return (sum(data) + checksum) % 256
        else:
            return (sum(map(ord, data)) + checksum) % 256

    # For CRC algorithm
    crctable = [
        0x0000, 0x1021, 0x2042, 0x3063, 0x4084, 0x50a5, 0x60c6, 0x70e7,
        0x8108, 0x9129, 0xa14a, 0xb16b, 0xc18c, 0xd1ad, 0xe1ce, 0xf1ef,
        0x1231, 0x0210, 0x3273, 0x2252, 0x52b5, 0x4294, 0x72f7, 0x62d6,
        0x9339, 0x8318, 0xb37b, 0xa35a, 0xd3bd, 0xc39c, 0xf3ff, 0xe3de,
        0x2462, 0x3443, 0x0420, 0x1401, 0x64e6, 0x74c7, 0x44a4, 0x5485,
        0xa56a, 0xb54b, 0x8528, 0x9509, 0xe5ee, 0xf5cf, 0xc5ac, 0xd58d,
        0x3653, 0x2672, 0x1611, 0x0630, 0x76d7, 0x66f6, 0x5695, 0x46b4,
        0xb75b, 0xa77a, 0x9719, 0x8738, 0xf7df, 0xe7fe, 0xd79d, 0xc7bc,
        0x48c4, 0x58e5, 0x6886, 0x78a7, 0x0840, 0x1861, 0x2802, 0x3823,
        0xc9cc, 0xd9ed, 0xe98e, 0xf9af, 0x8948, 0x9969, 0xa90a, 0xb92b,
        0x5af5, 0x4ad4, 0x7ab7, 0x6a96, 0x1a71, 0x0a50, 0x3a33, 0x2a12,
        0xdbfd, 0xcbdc, 0xfbbf, 0xeb9e, 0x9b79, 0x8b58, 0xbb3b, 0xab1a,
        0x6ca6, 0x7c87, 0x4ce4, 0x5cc5, 0x2c22, 0x3c03, 0x0c60, 0x1c41,
        0xedae, 0xfd8f, 0xcdec, 0xddcd, 0xad2a, 0xbd0b, 0x8d68, 0x9d49,
        0x7e97, 0x6eb6, 0x5ed5, 0x4ef4, 0x3e13, 0x2e32, 0x1e51, 0x0e70,
        0xff9f, 0xefbe, 0xdfdd, 0xcffc, 0xbf1b, 0xaf3a, 0x9f59, 0x8f78,
        0x9188, 0x81a9, 0xb1ca, 0xa1eb, 0xd10c, 0xc12d, 0xf14e, 0xe16f,
        0x1080, 0x00a1, 0x30c2, 0x20e3, 0x5004, 0x4025, 0x7046, 0x6067,
        0x83b9, 0x9398, 0xa3fb, 0xb3da, 0xc33d, 0xd31c, 0xe37f, 0xf35e,
        0x02b1, 0x1290, 0x22f3, 0x32d2, 0x4235, 0x5214, 0x6277, 0x7256,
        0xb5ea, 0xa5cb, 0x95a8, 0x8589, 0xf56e, 0xe54f, 0xd52c, 0xc50d,
        0x34e2, 0x24c3, 0x14a0, 0x0481, 0x7466, 0x6447, 0x5424, 0x4405,
        0xa7db, 0xb7fa, 0x8799, 0x97b8, 0xe75f, 0xf77e, 0xc71d, 0xd73c,
        0x26d3, 0x36f2, 0x0691, 0x16b0, 0x6657, 0x7676, 0x4615, 0x5634,
        0xd94c, 0xc96d, 0xf90e, 0xe92f, 0x99c8, 0x89e9, 0xb98a, 0xa9ab,
        0x5844, 0x4865, 0x7806, 0x6827, 0x18c0, 0x08e1, 0x3882, 0x28a3,
        0xcb7d, 0xdb5c, 0xeb3f, 0xfb1e, 0x8bf9, 0x9bd8, 0xabbb, 0xbb9a,
        0x4a75, 0x5a54, 0x6a37, 0x7a16, 0x0af1, 0x1ad0, 0x2ab3, 0x3a92,
        0xfd2e, 0xed0f, 0xdd6c, 0xcd4d, 0xbdaa, 0xad8b, 0x9de8, 0x8dc9,
        0x7c26, 0x6c07, 0x5c64, 0x4c45, 0x3ca2, 0x2c83, 0x1ce0, 0x0cc1,
        0xef1f, 0xff3e, 0xcf5d, 0xdf7c, 0xaf9b, 0xbfba, 0x8fd9, 0x9ff8,
        0x6e17, 0x7e36, 0x4e55, 0x5e74, 0x2e93, 0x3eb2, 0x0ed1, 0x1ef0,
    ]

    # CRC-16-CCITT
    def calc_crc(self, data, crc=0):
        for char in bytearray(data):
            crctbl_idx = ((crc >> 8) ^ char) & 0xff
            crc = ((crc << 8) ^ self.crctable[crctbl_idx]) & 0xffff
        return crc & 0xffff
