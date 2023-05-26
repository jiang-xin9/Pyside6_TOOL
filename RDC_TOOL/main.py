
# -*- coding: utf-8 -*-

"""
By: 清安无别事
使用命令为python编译的“resource.qrc”文件：

pyside6-rcc resources.qrc -o resources_rc.py

pyside6-uic main.ui -o ui_main.py

"""

# import os
# import time
from RDC_TOOL.modules import *
from RDC_TOOL.main_functions import *
from RDC_TOOL.main_functions.ota.run import OtaWindow
# from matploat import  pg_bat
from RDC_TOOL.widgets import *

os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
widgets = None
Message = "请检查路径是否填写"

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        # /////////////////////
        self.ser = Ser(widgets) # 实例化 serial
        # 创建一个快捷键对象，绑定 Enter 键
        shortcut = QShortcut(QKeySequence(Qt.Key_Return), self)
        # 添加一个快捷回车键，便于发送
        shortcut.activated.connect(self.ser.SendButton_clicked)
        # ///////// OTA ////////////
        self.ota = OtaWindow(widgets)
        # /////////////////////
        self.charts = ChartData()
        self.serial_thread = None
        # /////////////////////

        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        title = "RDC-测数组-数据处理工具"
        description = "RDC-研发部-测试组-数据处理工具"
        # APPLY TEXTS
        self.completer()
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_widgets.clicked.connect(self.buttonClick)
        widgets.btn_ota.clicked.connect(self.buttonClick)
        widgets.btn_document.clicked.connect(self.buttonClick)

        # ///////////////////////////////////////////////////////////////
        # 皮肤切换
        widgets.btn_exit.clicked.connect(self.buttonClick)
        # 获取曲线图的csv路径及文件
        widgets.btn_open_csv.clicked.connect(self.get_image_filepath)
        # 生成曲线图
        widgets.btn_create_image.clicked.connect(self.create_image)
        # 检测曲线图的文件路径是否改变
        widgets.lineEdit.textChanged.connect(self.charts_data_combox)
        # 清除图表
        widgets.btn_clear_image.clicked.connect(self.clear_image)
        # 获取文件路径
        widgets.btn_get.clicked.connect(self.get_line_filepath)
        # 保存info筛选的数据
        widgets.btn_get_all_data.clicked.connect(self.save_info_csv_data)
        # bat跳电情况
        widgets.btn_bat_jump.clicked.connect(self.get_btn_bat_jump)
        # warn情况
        widgets.btn_error.clicked.connect(self.warn_data)
        # info跳电
        widgets.btn_chang_jump.clicked.connect(self.get_info_battery_jump)
        # info充放电时长
        widgets.btn_time.clicked.connect(self.get_info_batterry_time)
        # 充电状态
        widgets.btn_status.clicked.connect(self.get_chanrge_stutas)
        # 打开COM升级的文件
        # widgets.Com_Open_file.clicked.connect(self.Com_file)
        widgets.Command_select.currentIndexChanged.connect(self.ota_combox)

        # ///////////////////////////////////////////////////////////////
        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # SHOW APP
        self.show()
        self.useCustomTheme = True

        # SET THEME AND HACKS
        if self.useCustomTheme:
            # LOAD AND APPLY STYLE
            # UIFunctions.theme(self, themeFile, True)
            UIFunctions.theme(self, ':/themes/py_dracula_light.qss', True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))


    # ///////////////////////////////////////////////////////////////

    def get_path(self):
        path = self.ui.line_filepath.text()
        return path

    def instantiation(self, class_, def_, *args, **kwargs):
        """各类实例化"""
        path = self.get_path()
        self.clear_TextEdit()
        if path:
            datas = getattr(class_, def_)(path, *args, **kwargs)
            if datas:
                return datas
            else:
                self.insert_TextEdit("没有数据,请检查正则是否匹配到了数据")
        else:
            self.show_messagebox()

    def other_data(self):
        data1 = self.ui.line_data1.text()
        data2 = self.ui.line_data2.text()
        if data1 and data2:
            return {"data1":data1, "data2":data2}
        else:
            self.show_messagebox("请检查参数是否填写")

    def get_btn_bat_jump(self):
        """bat跳电情况"""
        bat_data = self.instantiation(ALL_DATA(), 'get_bat_battery_data')
        filepath = self.get_path()
        self.clear_TextEdit()   # 清空之前的数据
        if bat_data:
            for value in bat_data:
                self.insert_TextEdit(value + '\n')
        if filepath:
            pg_bat(filepath)    # 写入图表，空数据的时候会退出
        else:
            pass

    def get_info_batterry_time(self):
        """info充放电时长"""
        data = self.other_data()
        time_data = self.instantiation(ALL_DATA(), 'get_info_battary_time', data['data1'], data['data2'])
        if time_data:
            self.insert_TextEdit("{}".format(time_data))

    def get_info_battery_jump(self):
        """info跳电情况"""
        datas = self.instantiation(ALL_DATA(), 'get_battary_jump')
        if datas:
            for value in datas:
                self.cursor_text()
                self.insert_TextEdit(value + '\n')

        if self.get_path():
            info_batt(self.get_path())  # 写入图表，空数据的时候会退出

    def get_chanrge_stutas(self):
        """充电状态"""
        datas = self.instantiation(ALL_DATA(), 'get_charge_data')
        if datas:
            for value in datas:
                self.cursor_text()
                self.insert_TextEdit(value['vol'] + '\n')
                self.insert_TextEdit(value['cur'] + '\n')
                self.insert_TextEdit(value['status'] + '\n')

    def warn_data(self):
        """告警"""
        data = self.other_data()
        if data:
            datas = self.instantiation(ALL_DATA(), 'get_warn_data', data['data1'], data['data2'])
            if datas:
                for value in datas:
                    self.cursor_text()
                    self.insert_TextEdit(value + '\n')

    # ///////////////////////////////////////////////////////////////

    def get_file_path(self, name):
        # 保存路径+名称
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(None, "选择文件", "",
                                                  "All Files (*);;Text Files (*.txt);;Image Files (*.log)",
                                                  options=options)
        if fileName:
            name.setText(fileName)

    def cursor_text(self):
        """定位光标"""
        cursor = self.ui.textEdit_2.textCursor()
        cursor.movePosition(QTextCursor.End)
        self.ui.textEdit_2.setTextCursor(cursor)

    # 工具页写入文本
    def insert_TextEdit(self, text):
        self.ui.textEdit_2.insertPlainText(text)

    def clear_TextEdit(self):
        # 清除文本
        text = self.ui.textEdit_2.toPlainText()
        if text != None:
            self.ui.textEdit_2.clear()

    def get_line_filename(self):
        # 获取文件名
        self.get_file_path(self.ui.line_filename)

    def get_line_filepath(self):
        # 获取文件路径
        self.get_file_path(self.ui.line_filepath)

    def get_image_filepath(self):
        # 获取图形的csv路径
        self.get_file_path(self.ui.lineEdit)

    def save_info_csv_data(self):
        read = RE_Data()
        line1 = self.ui.line_data1.text()
        line2 = self.ui.line_data2.text()
        get_path_name = self.ui.line_filepath.text()
        save_path_name = self.ui.line_filename.text()
        if get_path_name:
            if save_path_name:  # 如果获取到保存路径
                if line1 and line2:  # 有参数，写入到指定路径
                    read.read_data(get_path_name, line1, line2, save_path_name)
                else:
                    self.show_messagebox('请检查参数是否填写')
            else:  # 没有保存路径
                if line1 and line2:  # 有参数，写入到先对路径
                    read.read_data(get_path_name, line1, line2, csv_sys)
                else:
                    self.show_messagebox('请检查参数是否填写')
        else:
            self.show_messagebox()

    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW WIDGETS PAGE
        if btnName == "btn_widgets":
            widgets.stackedWidget.setCurrentWidget(widgets.widgets)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW NEW PAGE
        if btnName == "btn_ota":
            widgets.stackedWidget.setCurrentWidget(widgets.ota) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

        if btnName == "btn_document":
            widgets.stackedWidget.setCurrentWidget(widgets.Real_time_charts)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU

        if btnName == "btn_exit":
            if self.useCustomTheme:
                # themeFile = os.path.abspath(os.path.join(self.absPath, "themes\py_dracula_dark.qss"))
                # UIFunctions.theme(self, themeFile, True)
                UIFunctions.theme(self, ':/themes/py_dracula_dark.qss', True)
                # SET HACKS
                AppFunctions.setThemeHack(self)
                self.useCustomTheme = False
            else:
                # themeFile = os.path.abspath(os.path.join(self.absPath, "themes\py_dracula_light.qss"))
                UIFunctions.theme(self, ':/themes/py_dracula_light.qss', True)
                # UIFunctions.theme(self, themeFile, True)
                # SET HACKS
                AppFunctions.setThemeHack(self)
                self.useCustomTheme = True

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')


    # RESIZE EVENTS
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    def show_messagebox(self, Message=Message):
        QMessageBox.information(self, "提示信息", Message, QMessageBox.Yes | QMessageBox.No,
                                QMessageBox.Yes)


    def get_image_text_file(self):
        # 获取图形的文本路径
        path = widgets.lineEdit.text()
        return path

    def get_image_combox_text(self):
        # 获取combox文本
        text = widgets.btn_combox_image.currentText()
        text1 = widgets.btn_combox_image1.currentText()
        return text, text1

    # 曲线图
    def create_image(self):
        # 添加图表
        if self.get_image_combox_text()[0] != self.get_image_combox_text()[1]:
            self.datas = Csv_datas_Thread(path=self.get_image_text_file(),
                                          text=self.get_image_combox_text()[0],
                                          text1=self.get_image_combox_text()[1])
            self.datas.update_signal.connect(self.create_datas_image)
            self.datas.start()
        else:
            self.datas = Csv_datas_Thread(path=self.get_image_text_file(),
                                          text=self.get_image_combox_text()[0])
            self.datas.update_signal.connect(self.create_datas_image)
            self.datas.start()

    def create_datas_image(self, datas):
        # 给定charts_data数据
        if self.get_image_combox_text()[0] != self.get_image_combox_text()[1]:
            # print(datas[self.get_image_combox_text()[0]])
            # print(datas[self.get_image_combox_text()[1]])
            self.charts.update_chart(win=widgets.widget_2,
                        datas=datas[self.get_image_combox_text()[0]],
                        datas1=datas[self.get_image_combox_text()[1]],
                        title=self.get_image_combox_text()[0],
                        title1=self.get_image_combox_text()[1]
                        )
        else:
            self.charts.update_chart(win=widgets.widget_2,
                        datas=datas,
                        title=self.get_image_combox_text()[0]
                        )

    def clear_image(self):
        # 清除图表内容
        self.charts.clear_chart()

    def charts_data_combox(self):
        # 调用线程实现下拉框自动填补
        self.thread = Csv_header_Thread(self.get_image_text_file())
        self.thread.update_signal.connect(self.create_combox)
        self.thread.start()

    def create_combox(self, datas):
        # 添加数据
        if self.get_image_combox_text()[0] and self.get_image_combox_text()[1]:
            widgets.btn_combox_image.clear()    # 判断是否有值，如果有则清空
            widgets.btn_combox_image.clear()

        widgets.btn_combox_image.addItems(datas)
        widgets.btn_combox_image1.addItems(datas)

    # ///////////////////////////OTA//////////////
    def ota_combox(self):
        self.ui.lineEdit_3.setText(widgets.Command_select.currentText())
    # /////////////////////////////////////////////////////

    # MOUSE CLICK EVENTS
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '请确认', "请确认关闭", QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
            # 退出应用程序
            QApplication.quit()
        else:
            event.ignore()

    def completer(self):
        """自动补全"""
        list_ = ['charge', 'warn', 'batterry', 'motor', 'imu', 'water sensor']
        self.comp = QCompleter()
        # 设置自动完成的模型（例如 QStringListModel）
        model = QStringListModel()
        # 加入提示
        model.setStringList(list_)
        self.comp.setModel(model)
        # 获取 QCompleter 的下拉提示框
        popup = self.comp.popup()
        popup.setFixedHeight(30)
        # 设置 QListView 的样式
        popup.setStyleSheet('background-color: #6272a4;'
                            'color: #f8f8f2;'
                            'font-size: 15px;')
        self.ui.line_data1.setCompleter(self.comp)
        self.ui.line_data2.setCompleter(self.comp)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(":/images/images/images/ui图标.png"))
    window = MainWindow()
    sys.exit(app.exec())
