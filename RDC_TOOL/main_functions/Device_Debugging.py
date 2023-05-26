# -*- coding: utf-8 -*-
# https://blog.csdn.net/weixin_52040868
# 公众号：测个der
# 微信：qing_an_an

# import serial
# import sys
# import msvcrt
# import threading

# import re
import binascii
from PySide6.QtGui import QShortcut
from RDC_TOOL.main_functions import *
from RDC_TOOL.main_functions.config import sys_
from RDC_TOOL.main_functions.Realtime_Charts import DataPlotWidget
from PySide6.QtSerialPort import QSerialPort,QSerialPortInfo


class Ser():
    def __init__(self, ui):
        self.ui = ui    #
        self.ch = DataPlotWidget(self.ui)
        # 设置实例
        self.CreateItems()
        # 设置信号与槽
        self.CreateSignalSlot()
        self.time_ = time.strftime("%Y_%m_%d_%H_%M_%S")

    # 设置实例
    def CreateItems(self):
        # Qt 串口类
        self.com = QSerialPort()

    # 设置信号与槽
    def CreateSignalSlot(self):
        self.ui.Com_Open_Button.clicked.connect(self.Com_Open_Button_clicked)
        self.ui.Com_Close_Button.clicked.connect(self.Com_Close_Button_clicked)
        self.ui.Send_Button.clicked.connect(self.SendButton_clicked)
        self.ui.Chart_btn.clicked.connect(self.SendButton_clicked)  # Charts界面发送数据
        self.ui.Com_Refresh_Button.clicked.connect(self.Com_Refresh_Button_Clicked)
        self.com.readyRead.connect(self.Com_Receive_Data)  # 接收数据
        self.ui.hexSending_checkBox.stateChanged.connect(self.hexShowingClicked)
        self.ui.hexSending_checkBox.stateChanged.connect(self.hexSendingClicked)
        self.ui.ClearButton.clicked.connect(self.Clear_clicked)
        # self.ui.pushButton_2.clicked.connect(self.yymal)    # yaml

    # def yymal(self):    # 下拉框
    #     self.ui.Command_select.addItems(['meas','log'])

    def Get_Com_Send_Data(self):
        txData = self.ui.textEdit_Send.toPlainText()+ '\n'    # 获取发送数据
        lineData = self.ui.lineEdit_3.text()    # 获取发送数据
        chart_line = self.ui.Chart_line.text()
        if txData and lineData is not None and bool(chart_line) == False:     # 如果lineData不为空
            return txData
        elif chart_line and txData is not None and bool(lineData) == False:
            return chart_line + '\n'
        else:   # 不为空则返回lineData
            return lineData + '\n'

    # 串口发送数据
    def Com_Send_Data(self):
        txData = self.Get_Com_Send_Data()
        if len(txData) == 0:
            return
        if self.ui.hexSending_checkBox.isChecked() == False:
            self.com.write(txData.encode('UTF-8'))
        else:
            Data = txData.replace(' ', '')
            # 如果16进制不是偶数个字符, 去掉最后一个, [ ]左闭右开
            if len(Data) % 2 == 1:
                Data = Data[0:len(Data) - 1]
            # 如果遇到非16进制字符
            if Data.isalnum() is False:
                QMessageBox.critical(self, '错误', '包含非十六进制数')
            try:
                hexData = binascii.a2b_hex(Data)
            except:
                QMessageBox.critical(self, '错误', '转换编码错误')
                return
            # 发送16进制数据, 发送格式如 ‘31 32 33 41 42 43’, 代表'123ABC'
            try:
                self.com.write(hexData)
            except:
                QMessageBox.critical(self, '异常', '十六进制发送错误')
                return

    # 串口接收数据
    def Com_Receive_Data(self):

        try:
            rxData = bytes(self.com.readAll())
        except:
            QMessageBox.critical(self, '严重错误', '串口接收数据错误')
        if self.ui.hexShowing_checkBox.isChecked() == False:
            try:
                self.ui.textEdit_Recive.insertPlainText(rxData.decode('UTF-8'))

                with open(sys_ + f"\\{self.time_}.log", 'a', encoding='utf-8') as w:
                        w.write(rxData.decode('UTF-8'))
                # print(rxData.decode('UTF-8'))
                match = re.search(r'\d+\.\d+', rxData.decode('UTF-8'))
                if match:
                    number = match.group()
                    self.ch.update_data(number)
                # 滚动到底部并保持光标可见
                self.ui.textEdit_Recive.moveCursor(QTextCursor.End)
                self.ui.textEdit_Recive.ensureCursorVisible()

                # 滚动条自动滚动到底部
                scrollbar = self.ui.textEdit_Recive.verticalScrollBar()
                scrollbar.setValue(scrollbar.maximum())
            except:
                pass
        else:
            Data = binascii.b2a_hex(rxData).decode('ascii')
            # re 正则表达式 (.{2}) 匹配两个字母
            hexStr = ' 0x'.join(re.findall('(.{2})', Data))
            # 补齐第一个 0x
            hexStr = '0x' + hexStr
            self.ui.textEdit_Recive.insertPlainText(hexStr)
            self.ui.textEdit_Recive.insertPlainText(' ')

    # 串口刷新
    def Com_Refresh_Button_Clicked(self):
        self.ui.Com_Name_Combo.clear()
        com = QSerialPort()
        com_list = QSerialPortInfo.availablePorts()
        for info in com_list:
            com.setPort(info)
            if com.open(QSerialPort.ReadWrite):
                self.ui.Com_Name_Combo.addItem(info.portName())
                com.close()

    # 16进制显示按下
    def hexShowingClicked(self):
        if self.ui.hexShowing_checkBox.isChecked() == True:
            # 接收区换行
            self.ui.textEdit_Recive.insertPlainText('\n')


    # 16进制发送按下
    def hexSendingClicked(self):
        if self.ui.hexSending_checkBox.isChecked() == True:
            pass

    # 发送按钮按下
    def SendButton_clicked(self):
        self.Com_Send_Data()

    # 清除内容
    def Clear_clicked(self):
        self.ui.textEdit_Recive.clear()

    # 串口刷新按钮按下
    def Com_Open_Button_clicked(self):
        #### com Open Code here ####
        comName = self.ui.Com_Name_Combo.currentText()
        comBaud = int(self.ui.Com_Baud_Combo.currentText())
        self.com.setPortName(comName)
        try:
            if self.com.open(QSerialPort.ReadWrite) == False:
                QMessageBox.critical(self, '严重错误', '串口打开失败')
                return
        except:
            QMessageBox.critical(self, '严重错误', '串口打开失败')
            return
        self.ui.Com_Close_Button.setEnabled(True)
        self.ui.Com_Open_Button.setEnabled(False)
        self.ui.Com_Refresh_Button.setEnabled(False)
        self.ui.Com_Name_Combo.setEnabled(False)
        self.ui.Com_Baud_Combo.setEnabled(False)
        self.ui.Com_isOpenOrNot_Label.setText('  已打开')
        self.com.setBaudRate(comBaud)

    def Com_Close_Button_clicked(self):
        self.com.close()
        self.ui.Com_Close_Button.setEnabled(False)
        self.ui.Com_Open_Button.setEnabled(True)
        self.ui.Com_Refresh_Button.setEnabled(True)
        self.ui.Com_Name_Combo.setEnabled(True)
        self.ui.Com_Baud_Combo.setEnabled(True)
        self.ui.Com_isOpenOrNot_Label.setText('  已关闭')




# class SerialTerminal(object):
#
#     def __init__(self,COM, PORT):
#         self.COM = COM
#         self.PORT = PORT
#
#     def Getch(self):
#         """Get Keyboard Byte"""
#         return msvcrt.getch().decode()
#
#     def Start(self):
#         """RUN"""
#         self.ser = serial.Serial(self.COM, self.PORT)  # 不使用数据终端准备  # 设置串口名称和波特率
#         self.ser.write(f"\n".encode())
#
#         self.Read_thread = threading.Thread(target=self.Read_serial)
#         self.Read_thread.daemon = True
#         self.Read_thread.start()
#
#         # 主线程等待键盘输入
#         while True:
#             ch = self.Getch()
#             # if ch == b'q':
#             if ord(ch) == 3:  # 按下Ctrl+C键的ASCII码为3
#                 # ESC退出循环
#                 break
#             self.ser.write(ch.encode())
#
#     def Read_serial(self):
#         while True:
#             try:
#                 count = self.ser.inWaiting()
#                 if count != 0:
#                     # 读取内容并回显
#                     recv = self.ser.read(count)
#                     print(recv.decode(), end="", flush=True)
#             except UnicodeDecodeError as e:
#                 pass

# if __name__ == '__main__':
#     ter = SerialTerminal('COM3', 115200)
#     ter.Start()

