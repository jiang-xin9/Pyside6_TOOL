# -*- coding: utf-8 -*-
# https://blog.csdn.net/weixin_52040868
# 公众号：测个der
# 微信：qing_an_an
import os
import time
import serial
import logging
import serial.tools.list_ports
from RDC_TOOL.main_functions.ota.Modem import Modem
from PySide6 import QtWidgets
from PySide6.QtCore import Signal, QThread


class SerialModule(object):
    def __init__(self):
        self.serial_io = serial.Serial()

    def listPorts(self):
        ports_list = sorted(serial.tools.list_ports.comports())
        return [list(port)[0] for port in ports_list] or None
        # if len(ports_list) > 0:
        #     return [list(port)[0] for port in ports_list]
        # else:
        #     return None

    def openPort(self, port, baudrate="115200", parity="N", bytesize=8, stopbits=1):
        # serial_io.port = "COM24"
        self.serial_io.port = port
        self.serial_io.baudrate = baudrate
        self.serial_io.parity = parity
        self.serial_io.bytesize = bytesize
        self.serial_io.stopbits = stopbits
        self.serial_io.timeout = 2
        try:
            self.serial_io.open()
        except Exception as e:
            raise Exception("Failed to open serial port!")

    def readPort(self, size, timeout=3):
        self.serial_io.timeout = timeout
        return self.serial_io.read(size) or None

    def writePort(self, data, timeout=3):
        self.serial_io.writeTimeout = timeout
        return self.serial_io.write(data)

    def readLinePort(self, timeout=3):
        self.serial_io.timeout = timeout
        return self.serial_io.readline() or None

    def readAllPort(self, timeout=3):
        self.serial_io.timeout = timeout
        return self.serial_io.readall() or None

    def readValidPort(self):
        count = self.serial_io.inWaiting()
        if count != 0:
            return self.serial_io.read(count) or None
        else:
            return None

    def closePort(self):
        self.serial_io.close()


class YmodemThread(QThread):
    sigStatus = Signal(str)
    sigProgressBar = Signal(int)
    sigEnd = Signal()

    def __init__(self, serial, port, file, mode):
        super().__init__()
        self.serial = serial
        self.port = port
        self.file = file
        self.mode = mode
        self.last_task_name = ""
        self.current_task_start_time = -1

    def progress_bar(self, task_index, task_name, total, success, failed):
        progress = (success / total) * 100
        self.sigProgressBar.emit(int(progress))

        if success == 1:
            self.current_task_start_time = time.perf_counter()

        if self.mode == 'ymodem':
            real_block = 133  # 128 + 5
        else:
            real_block = 1029  # 1024 + 5

        cost = time.perf_counter() - self.current_task_start_time
        bps = (success - 1) * real_block / 1024 / cost
        statusMsg = "速度: {:.2f}KB/s  时间: {:.2f}s".format(bps, cost)
        self.sigStatus.emit(statusMsg)

    def run(self):
        try:
            self.serial.openPort(self.port)
        except:
            self.sigStatus.emit("端口异常")
            return
        retry = 0
        upgrade = False
        while True:
            data = self.serial.readPort(1, timeout=2)
            if data == b'\x43':
                upgrade = True
                break
            elif data != None:
                continue
            else:  # 读空
                if retry >= 2:
                    self.sigStatus.emit("发送失败")
                    break
                else:
                    self.serial.writePort("upgrade\r\n".encode("utf-8"))
                retry += 1
        if upgrade == True:
            sender = Modem(self.serial.readPort, self.serial.writePort, self.mode)
            sender.send([self.file], callback=self.progress_bar)
            self.sigStatus.emit("发送成功")
            # self.msleep(500)
        self.serial.closePort()
        self.sigEnd.emit()  # 发送结果


class CmdThread(QThread):
    sigStatus = Signal(str)
    sigEnd = Signal()

    def __init__(self, serial, port, cmd):
        super().__init__()
        self.serial = serial
        self.port = port
        self.cmd = cmd + '\r\n'

    def run(self):
        self.serial.openPort(self.port)
        self.serial.writePort(self.cmd.encode("utf-8"))
        data = self.serial.readLinePort(1)
        if data:
            self.sigStatus.emit(data.decode("utf-8"))
        else:
            self.sigStatus.emit("无响应")
        self.serial.closePort()
        self.sigEnd.emit()  # 发送结果


class OtaWindow():
    def __init__(self, ui):
        # window init
        super(OtaWindow, self).__init__()
        self.ui = ui
        self.ui.progressBar.setProperty("value", 0)

        # ota init
        self.ui.Com_Open_file.clicked.connect(self.openFile)
        self.ui.pushButton_2.clicked.connect(self.checkPortAndPath)
        # self.ui.Com_Name_Combo.installEventFilter(self)
        self.serial = SerialModule()

    # def closeEvent(self, event):
    #     event.ignore()

    def eventFilter(self, watched, event):
        if (watched == self.ui.Com_Name_Combo and event.type() == event.MouseButtonPress):
            # print('鼠标事件')
            self.listCom()
            # return True
        return super(OtaWindow, self).eventFilter(watched, event)

    def openFile(self):
        dlg = QtWidgets.QFileDialog()
        dlg.setFileMode(QtWidgets.QFileDialog.AnyFile)
        filenames = None
        if dlg.exec_():
            filenames = dlg.selectedFiles()
            if filenames != None:
                self.ui.Com_file_line.setText(filenames[0])

    def listCom(self):
        ports = self.serial.listPorts()
        if ports:
            for port in ports:
                self.ui.Com_Name_Combo.addItem(port)

    def checkPortAndPath(self):
        self.ui.Com_isOpenOrNot_Label.clear()
        self.ui.progressBar.setValue(0)
        if self.ui.Com_Name_Combo.count() == 0:
            self.ui.Com_isOpenOrNot_Label.showMessage("请选择串口")
            return
        file_path = self.ui.Com_file_line.text()
        # print(file_path)
        if file_path == '':
            self.ui.Com_isOpenOrNot_Label.showMessage("请选择文件或输入命令")
            return
        if os.path.exists(file_path):
            self.upgradeStart(file_path)
        else:
            self.sendCmd(file_path)

    def upgradeStart(self, file):
        self.ui.pushButton_2.setText("发送中...")
        self.ui.pushButton_2.setEnabled(False)
        port = self.ui.Com_Name_Combo.currentText()
        if self.ui.comboBox.currentText() == '128':
            mode = 'ymodem'
        else:
            mode = 'ymodem1k'
        self.yThd = YmodemThread(self.serial, port, file, mode)
        self.yThd.sigStatus.connect(self.ui.Com_isOpenOrNot_Label.setText)
        self.yThd.sigProgressBar.connect(self.ui.progressBar.setValue)
        self.yThd.sigEnd.connect(self.upgradeEnd)
        self.yThd.start()

    def upgradeEnd(self):
        self.ui.pushButton_2.setText("发送")
        self.ui.pushButton_2.setEnabled(True)

    def sendCmd(self, cmd):
        # print("发送命令")
        self.ui.pushButton_2.setText("发送中...")
        self.ui.pushButton_2.setEnabled(False)
        port = self.ui.Com_Name_Combo.currentText()
        self.cmdThd = CmdThread(self.serial, port, cmd)
        self.cmdThd.sigStatus.connect(self.ui.Com_isOpenOrNot_Label.setText)
        self.cmdThd.sigEnd.connect(self.upgradeEnd)
        self.cmdThd.start()


