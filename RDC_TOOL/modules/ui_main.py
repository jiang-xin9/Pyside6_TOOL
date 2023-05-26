# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTextEdit, QVBoxLayout,
    QWidget)
from . import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 833)
        MainWindow.setMinimumSize(QSize(940, 560))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 11pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	"
                        "\n"
"	background-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	backgrou"
                        "nd-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	backgr"
                        "ound-color: rgb(189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraCont"
                        "ent{\n"
"	border-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49,"
                        " 57); border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);"
                        "\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
""
                        "	background-color: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selectio"
                        "n-background-color: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: ma"
                        "rgin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bot"
                        "tom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59,"
                        " 72);	\n"
"	background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: pad"
                        "ding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border:"
                        " none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton *"
                        "/\n"
"QCommandLinkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.horizontalLayout_12 = QHBoxLayout(self.styleSheet)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setStyleSheet(u"border-image: url(:/images/images/images/ui\u56fe\u6807.png);\n"
"border-radius: 21px;")
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_widgets = QPushButton(self.topMenu)
        self.btn_widgets.setObjectName(u"btn_widgets")
        sizePolicy.setHeightForWidth(self.btn_widgets.sizePolicy().hasHeightForWidth())
        self.btn_widgets.setSizePolicy(sizePolicy)
        self.btn_widgets.setMinimumSize(QSize(0, 45))
        self.btn_widgets.setFont(font)
        self.btn_widgets.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_widgets.setLayoutDirection(Qt.LeftToRight)
        self.btn_widgets.setStyleSheet(u"\n"
"background-image: url(:/icons/images/icons/cil-chart.png);")

        self.verticalLayout_8.addWidget(self.btn_widgets)

        self.btn_ota = QPushButton(self.topMenu)
        self.btn_ota.setObjectName(u"btn_ota")
        sizePolicy.setHeightForWidth(self.btn_ota.sizePolicy().hasHeightForWidth())
        self.btn_ota.setSizePolicy(sizePolicy)
        self.btn_ota.setMinimumSize(QSize(0, 45))
        self.btn_ota.setFont(font)
        self.btn_ota.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_ota.setLayoutDirection(Qt.LeftToRight)
        self.btn_ota.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-arrow-circle-top.png);")

        self.verticalLayout_8.addWidget(self.btn_ota)

        self.btn_document = QPushButton(self.topMenu)
        self.btn_document.setObjectName(u"btn_document")
        sizePolicy.setHeightForWidth(self.btn_document.sizePolicy().hasHeightForWidth())
        self.btn_document.setSizePolicy(sizePolicy)
        self.btn_document.setMinimumSize(QSize(0, 45))
        self.btn_document.setFont(font)
        self.btn_document.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_document.setLayoutDirection(Qt.LeftToRight)
        self.btn_document.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-file.png);")

        self.verticalLayout_8.addWidget(self.btn_document)

        self.btn_exit = QPushButton(self.topMenu)
        self.btn_exit.setObjectName(u"btn_exit")
        sizePolicy.setHeightForWidth(self.btn_exit.sizePolicy().hasHeightForWidth())
        self.btn_exit.setSizePolicy(sizePolicy)
        self.btn_exit.setMinimumSize(QSize(0, 45))
        self.btn_exit.setFont(font)
        self.btn_exit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_exit.setLayoutDirection(Qt.LeftToRight)
        self.btn_exit.setStyleSheet(u"\n"
"background-image: url(:/icons/images/icons/cil-loop-circular.png);")

        self.verticalLayout_8.addWidget(self.btn_exit)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font)
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_settings.png);")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_share = QPushButton(self.extraTopMenu)
        self.btn_share.setObjectName(u"btn_share")
        sizePolicy.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
        self.btn_share.setSizePolicy(sizePolicy)
        self.btn_share.setMinimumSize(QSize(0, 45))
        self.btn_share.setFont(font)
        self.btn_share.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_share.setLayoutDirection(Qt.LeftToRight)
        self.btn_share.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-share-boxed.png);")

        self.verticalLayout_11.addWidget(self.btn_share)

        self.btn_adjustments = QPushButton(self.extraTopMenu)
        self.btn_adjustments.setObjectName(u"btn_adjustments")
        sizePolicy.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
        self.btn_adjustments.setSizePolicy(sizePolicy)
        self.btn_adjustments.setMinimumSize(QSize(0, 45))
        self.btn_adjustments.setFont(font)
        self.btn_adjustments.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_adjustments.setLayoutDirection(Qt.LeftToRight)
        self.btn_adjustments.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_11.addWidget(self.btn_adjustments)

        self.btn_more = QPushButton(self.extraTopMenu)
        self.btn_more.setObjectName(u"btn_more")
        sizePolicy.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        self.btn_more.setSizePolicy(sizePolicy)
        self.btn_more.setMinimumSize(QSize(0, 45))
        self.btn_more.setFont(font)
        self.btn_more.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_more.setLayoutDirection(Qt.LeftToRight)
        self.btn_more.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_11.addWidget(self.btn_more)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon1)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon2)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font3.setPointSize(11)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon3)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"")
        self.horizontalLayout_6 = QHBoxLayout(self.home)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.textEdit_2 = QTextEdit(self.home)
        self.textEdit_2.setObjectName(u"textEdit_2")
        sizePolicy1.setHeightForWidth(self.textEdit_2.sizePolicy().hasHeightForWidth())
        self.textEdit_2.setSizePolicy(sizePolicy1)
        self.textEdit_2.setMinimumSize(QSize(500, 700))
        self.textEdit_2.setMaximumSize(QSize(600, 16777215))
        self.textEdit_2.setFont(font)
        self.textEdit_2.setStyleSheet(u"")

        self.horizontalLayout_6.addWidget(self.textEdit_2)

        self.frame_6 = QFrame(self.home)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(640, 700))
        self.frame_6.setStyleSheet(u"QFrame#frame_6{\n"
"	border: 1px solid #343b48;\n"
"	/*background-color: rgb(126, 199, 193);*/\n"
"	border-radius:20px;\n"
"\n"
"}\n"
"QFrame#frame_7{\n"
"	/*background-color: rgb(161, 217, 218);*/\n"
"	border-radius:20px;\n"
"\n"
"}\n"
"QFrame#frame_8{\n"
"	/*background-color: rgb(161, 217, 218);*/\n"
"	border-radius:20px;\n"
"\n"
"}\n"
"QPushButton {\n"
"	border-radius:20px;\n"
"	/*background-color: rgb(255, 255, 255);*/\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: black;\n"
"	background-color: rgb(207, 232, 232);\n"
"	padding-left: 15px;\n"
"}\n"
"QPushButton:pressed {\n"
"	/*color: white;*/\n"
"	background-color: rgb(189, 147, 249);\n"
"	border-style: inset;\n"
"	padding-left: 15px;\n"
"}\n"
"QLineEdit{\n"
"	/*color: rgb(0, 0, 0);*/\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius:15px;\n"
"}\n"
"QLabel#info_text{\n"
"	font-size:22px;\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_6)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(5, 5, 7, 5)
        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy3)
        self.frame_7.setStyleSheet(u"")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_7)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_5 = QSpacerItem(230, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_5)

        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy4)
        self.frame_9.setMinimumSize(QSize(100, 40))
        self.frame_9.setMaximumSize(QSize(100, 40))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(20, 0, 30, 0)
        self.label_15 = QLabel(self.frame_9)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(40, 40))
        self.label_15.setFont(font)
        self.label_15.setStyleSheet(u"image: url(:/icons/images/icons/cil-wallet.png);")
        self.label_15.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_15)

        self.info_text = QLabel(self.frame_9)
        self.info_text.setObjectName(u"info_text")
        self.info_text.setMinimumSize(QSize(47, 35))
        font4 = QFont()
        font4.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font4.setBold(False)
        font4.setItalic(False)
        self.info_text.setFont(font4)
        self.info_text.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.info_text)


        self.horizontalLayout_8.addWidget(self.frame_9)

        self.horizontalSpacer_6 = QSpacerItem(230, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_6)


        self.verticalLayout_22.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setSpacing(8)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(8, 0, 8, 0)
        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setSpacing(12)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(12, 0, 12, 0)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 5, -1, 5)
        self.label_10 = QLabel(self.frame_7)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(85, 30))
        self.label_10.setFont(font)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_10)

        self.line_filename = QLineEdit(self.frame_7)
        self.line_filename.setObjectName(u"line_filename")
        self.line_filename.setMinimumSize(QSize(284, 40))
        self.line_filename.setFont(font)
        self.line_filename.setStyleSheet(u"")

        self.horizontalLayout_10.addWidget(self.line_filename)


        self.verticalLayout_23.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(-1, 5, -1, 5)
        self.label_11 = QLabel(self.frame_7)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(85, 30))
        self.label_11.setFont(font)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.label_11)

        self.line_filepath = QLineEdit(self.frame_7)
        self.line_filepath.setObjectName(u"line_filepath")
        self.line_filepath.setMinimumSize(QSize(284, 40))
        self.line_filepath.setFont(font)
        self.line_filepath.setStyleSheet(u"")

        self.horizontalLayout_15.addWidget(self.line_filepath)


        self.verticalLayout_23.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(-1, 5, -1, 5)
        self.label_12 = QLabel(self.frame_7)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(85, 30))
        self.label_12.setFont(font)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.label_12)

        self.line_data1 = QLineEdit(self.frame_7)
        self.line_data1.setObjectName(u"line_data1")
        self.line_data1.setMinimumSize(QSize(284, 40))
        self.line_data1.setFont(font)
        self.line_data1.setStyleSheet(u"")

        self.horizontalLayout_17.addWidget(self.line_data1)


        self.verticalLayout_23.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(-1, 5, -1, 5)
        self.label_13 = QLabel(self.frame_7)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(85, 30))
        self.label_13.setFont(font)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.label_13)

        self.line_data2 = QLineEdit(self.frame_7)
        self.line_data2.setObjectName(u"line_data2")
        self.line_data2.setMinimumSize(QSize(284, 40))
        self.line_data2.setFont(font)
        self.line_data2.setStyleSheet(u"")

        self.horizontalLayout_18.addWidget(self.line_data2)


        self.verticalLayout_23.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(-1, 5, -1, 5)
        self.btn_get = QPushButton(self.frame_7)
        self.btn_get.setObjectName(u"btn_get")
        self.btn_get.setMinimumSize(QSize(200, 45))
        self.btn_get.setFont(font)
        self.btn_get.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_get.setStyleSheet(u"")

        self.horizontalLayout_19.addWidget(self.btn_get)

        self.btn_get_all_data = QPushButton(self.frame_7)
        self.btn_get_all_data.setObjectName(u"btn_get_all_data")
        self.btn_get_all_data.setMinimumSize(QSize(200, 45))
        self.btn_get_all_data.setFont(font)
        self.btn_get_all_data.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_get_all_data.setStyleSheet(u"")

        self.horizontalLayout_19.addWidget(self.btn_get_all_data)


        self.verticalLayout_23.addLayout(self.horizontalLayout_19)


        self.horizontalLayout_16.addLayout(self.verticalLayout_23)


        self.verticalLayout_22.addLayout(self.horizontalLayout_16)


        self.verticalLayout_21.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFont(font)
        self.frame_8.setStyleSheet(u"")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalSpacer_9 = QSpacerItem(170, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_9)

        self.frame_10 = QFrame(self.frame_8)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(200, 45))
        self.frame_10.setMaximumSize(QSize(16777215, 45))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.label_16 = QLabel(self.frame_10)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(10, 10, 180, 30))
        self.label_16.setFont(font)
        self.label_16.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.frame_10)

        self.horizontalSpacer_10 = QSpacerItem(170, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_10)


        self.verticalLayout_24.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(5, 5, 5, 5)
        self.btn_chang_jump = QPushButton(self.frame_8)
        self.btn_chang_jump.setObjectName(u"btn_chang_jump")
        self.btn_chang_jump.setMinimumSize(QSize(140, 45))
        self.btn_chang_jump.setFont(font)
        self.btn_chang_jump.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_23.addWidget(self.btn_chang_jump)

        self.btn_bat_jump = QPushButton(self.frame_8)
        self.btn_bat_jump.setObjectName(u"btn_bat_jump")
        self.btn_bat_jump.setMinimumSize(QSize(140, 45))
        self.btn_bat_jump.setFont(font)
        self.btn_bat_jump.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_23.addWidget(self.btn_bat_jump)

        self.btn_time = QPushButton(self.frame_8)
        self.btn_time.setObjectName(u"btn_time")
        self.btn_time.setMinimumSize(QSize(140, 45))
        self.btn_time.setFont(font)
        self.btn_time.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_23.addWidget(self.btn_time)


        self.verticalLayout_24.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(5, 5, 5, 5)
        self.btn_error = QPushButton(self.frame_8)
        self.btn_error.setObjectName(u"btn_error")
        self.btn_error.setMinimumSize(QSize(140, 45))
        self.btn_error.setFont(font)
        self.btn_error.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_24.addWidget(self.btn_error)

        self.btn_status = QPushButton(self.frame_8)
        self.btn_status.setObjectName(u"btn_status")
        self.btn_status.setMinimumSize(QSize(140, 45))
        self.btn_status.setFont(font)
        self.btn_status.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_24.addWidget(self.btn_status)

        self.btn_dazhaun = QPushButton(self.frame_8)
        self.btn_dazhaun.setObjectName(u"btn_dazhaun")
        self.btn_dazhaun.setMinimumSize(QSize(140, 45))
        self.btn_dazhaun.setFont(font)
        self.btn_dazhaun.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_24.addWidget(self.btn_dazhaun)


        self.verticalLayout_24.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(5, 5, 5, 5)
        self.start_vol_cur = QPushButton(self.frame_8)
        self.start_vol_cur.setObjectName(u"start_vol_cur")
        self.start_vol_cur.setMinimumSize(QSize(140, 45))
        self.start_vol_cur.setFont(font)
        self.start_vol_cur.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_25.addWidget(self.start_vol_cur)

        self.pushButton_8 = QPushButton(self.frame_8)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(140, 45))
        self.pushButton_8.setFont(font)
        self.pushButton_8.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_25.addWidget(self.pushButton_8)

        self.pushButton_10 = QPushButton(self.frame_8)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMinimumSize(QSize(140, 45))
        self.pushButton_10.setFont(font)
        self.pushButton_10.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_25.addWidget(self.pushButton_10)


        self.verticalLayout_24.addLayout(self.horizontalLayout_25)


        self.horizontalLayout_21.addLayout(self.verticalLayout_24)


        self.verticalLayout_21.addWidget(self.frame_8)


        self.horizontalLayout_6.addWidget(self.frame_6)

        self.stackedWidget.addWidget(self.home)
        self.widgets = QWidget()
        self.widgets.setObjectName(u"widgets")
        self.widgets.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.widgets)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.row_1 = QFrame(self.widgets)
        self.row_1.setObjectName(u"row_1")
        sizePolicy2.setHeightForWidth(self.row_1.sizePolicy().hasHeightForWidth())
        self.row_1.setSizePolicy(sizePolicy2)
        self.row_1.setFrameShape(QFrame.StyledPanel)
        self.row_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.row_1)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.frame_content_wid_1 = QFrame(self.row_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.frame_content_wid_1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(450, 30))
        self.lineEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_9.addWidget(self.lineEdit)

        self.btn_open_csv = QPushButton(self.frame_content_wid_1)
        self.btn_open_csv.setObjectName(u"btn_open_csv")
        self.btn_open_csv.setMinimumSize(QSize(120, 35))
        self.btn_open_csv.setFont(font)
        self.btn_open_csv.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_open_csv.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_open_csv.setIcon(icon4)

        self.horizontalLayout_9.addWidget(self.btn_open_csv)

        self.btn_combox_image = QComboBox(self.frame_content_wid_1)
        self.btn_combox_image.setObjectName(u"btn_combox_image")
        self.btn_combox_image.setMinimumSize(QSize(120, 35))

        self.horizontalLayout_9.addWidget(self.btn_combox_image)

        self.btn_combox_image1 = QComboBox(self.frame_content_wid_1)
        self.btn_combox_image1.setObjectName(u"btn_combox_image1")
        self.btn_combox_image1.setMinimumSize(QSize(120, 35))

        self.horizontalLayout_9.addWidget(self.btn_combox_image1)

        self.btn_create_image = QPushButton(self.frame_content_wid_1)
        self.btn_create_image.setObjectName(u"btn_create_image")
        self.btn_create_image.setMinimumSize(QSize(120, 35))
        self.btn_create_image.setFont(font)
        self.btn_create_image.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_create_image.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.horizontalLayout_9.addWidget(self.btn_create_image)

        self.btn_clear_image = QPushButton(self.frame_content_wid_1)
        self.btn_clear_image.setObjectName(u"btn_clear_image")
        self.btn_clear_image.setMinimumSize(QSize(120, 35))
        self.btn_clear_image.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.horizontalLayout_9.addWidget(self.btn_clear_image)


        self.verticalLayout_19.addWidget(self.frame_content_wid_1)


        self.verticalLayout.addWidget(self.row_1, 0, Qt.AlignTop)

        self.frame = QFrame(self.widgets)
        self.frame.setObjectName(u"frame")
        sizePolicy2.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy2)
        self.frame.setMinimumSize(QSize(1150, 0))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.widget_2 = QWidget(self.frame)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_16.addWidget(self.widget_2)


        self.verticalLayout.addWidget(self.frame)

        self.stackedWidget.addWidget(self.widgets)
        self.ota = QWidget()
        self.ota.setObjectName(u"ota")
        self.horizontalLayout_27 = QHBoxLayout(self.ota)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.frame_12 = QFrame(self.ota)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_34 = QVBoxLayout()
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_8 = QLabel(self.frame_12)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(120, 35))
        self.label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_22.addWidget(self.label_8)

        self.horizontalSpacer_3 = QSpacerItem(128, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_3)

        self.hexShowing_checkBox = QCheckBox(self.frame_12)
        self.hexShowing_checkBox.setObjectName(u"hexShowing_checkBox")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.hexShowing_checkBox.sizePolicy().hasHeightForWidth())
        self.hexShowing_checkBox.setSizePolicy(sizePolicy5)

        self.horizontalLayout_22.addWidget(self.hexShowing_checkBox)

        self.ClearButton = QPushButton(self.frame_12)
        self.ClearButton.setObjectName(u"ClearButton")
        self.ClearButton.setMinimumSize(QSize(120, 35))

        self.horizontalLayout_22.addWidget(self.ClearButton)


        self.verticalLayout_34.addLayout(self.horizontalLayout_22)

        self.textEdit_Recive = QTextEdit(self.frame_12)
        self.textEdit_Recive.setObjectName(u"textEdit_Recive")
        sizePolicy3.setHeightForWidth(self.textEdit_Recive.sizePolicy().hasHeightForWidth())
        self.textEdit_Recive.setSizePolicy(sizePolicy3)
        self.textEdit_Recive.setMinimumSize(QSize(450, 645))
        self.textEdit_Recive.setStyleSheet(u"QTextEdit#textEdit_Recive{\n"
"	border-radius: 10px;\n"
"	border: 1px solid black;\n"
"	background-color: rgb(241, 241, 241);\n"
"}")

        self.verticalLayout_34.addWidget(self.textEdit_Recive)


        self.horizontalLayout_29.addLayout(self.verticalLayout_34)


        self.horizontalLayout_27.addWidget(self.frame_12)

        self.frame_2 = QFrame(self.ota)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_2)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(275, 280))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.Com_Refresh_Label = QLabel(self.frame_5)
        self.Com_Refresh_Label.setObjectName(u"Com_Refresh_Label")
        self.Com_Refresh_Label.setMinimumSize(QSize(120, 35))
        self.Com_Refresh_Label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.Com_Refresh_Label)

        self.Com_Baud_Label = QLabel(self.frame_5)
        self.Com_Baud_Label.setObjectName(u"Com_Baud_Label")
        self.Com_Baud_Label.setMinimumSize(QSize(120, 35))
        self.Com_Baud_Label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.Com_Baud_Label)

        self.Com_Name_Label = QLabel(self.frame_5)
        self.Com_Name_Label.setObjectName(u"Com_Name_Label")
        self.Com_Name_Label.setMinimumSize(QSize(120, 35))
        self.Com_Name_Label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.Com_Name_Label)

        self.Com_Open_Label = QLabel(self.frame_5)
        self.Com_Open_Label.setObjectName(u"Com_Open_Label")
        self.Com_Open_Label.setMinimumSize(QSize(120, 35))
        self.Com_Open_Label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.Com_Open_Label)

        self.Com_Close_Label = QLabel(self.frame_5)
        self.Com_Close_Label.setObjectName(u"Com_Close_Label")
        self.Com_Close_Label.setMinimumSize(QSize(120, 35))
        self.Com_Close_Label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.Com_Close_Label)


        self.horizontalLayout_13.addLayout(self.verticalLayout_17)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.Com_Refresh_Button = QPushButton(self.frame_5)
        self.Com_Refresh_Button.setObjectName(u"Com_Refresh_Button")
        self.Com_Refresh_Button.setMinimumSize(QSize(120, 35))
        self.Com_Refresh_Button.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_20.addWidget(self.Com_Refresh_Button)

        self.Com_Baud_Combo = QComboBox(self.frame_5)
        self.Com_Baud_Combo.addItem("")
        self.Com_Baud_Combo.addItem("")
        self.Com_Baud_Combo.addItem("")
        self.Com_Baud_Combo.addItem("")
        self.Com_Baud_Combo.addItem("")
        self.Com_Baud_Combo.addItem("")
        self.Com_Baud_Combo.addItem("")
        self.Com_Baud_Combo.addItem("")
        self.Com_Baud_Combo.setObjectName(u"Com_Baud_Combo")
        self.Com_Baud_Combo.setMinimumSize(QSize(120, 35))
        self.Com_Baud_Combo.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_20.addWidget(self.Com_Baud_Combo)

        self.Com_Name_Combo = QComboBox(self.frame_5)
        self.Com_Name_Combo.setObjectName(u"Com_Name_Combo")
        self.Com_Name_Combo.setMinimumSize(QSize(120, 35))
        self.Com_Name_Combo.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_20.addWidget(self.Com_Name_Combo)

        self.Com_Open_Button = QPushButton(self.frame_5)
        self.Com_Open_Button.setObjectName(u"Com_Open_Button")
        self.Com_Open_Button.setMinimumSize(QSize(120, 35))
        self.Com_Open_Button.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_20.addWidget(self.Com_Open_Button)

        self.Com_Close_Button = QPushButton(self.frame_5)
        self.Com_Close_Button.setObjectName(u"Com_Close_Button")
        self.Com_Close_Button.setMinimumSize(QSize(120, 35))
        self.Com_Close_Button.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_20.addWidget(self.Com_Close_Button)


        self.horizontalLayout_13.addLayout(self.verticalLayout_20)


        self.horizontalLayout_26.addWidget(self.frame_5)

        self.frame_11 = QFrame(self.frame_2)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(275, 280))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_11)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 5, 0, 0)
        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_9 = QLabel(self.frame_11)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_9)

        self.label_14 = QLabel(self.frame_11)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_14)

        self.label_17 = QLabel(self.frame_11)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_17)


        self.horizontalLayout_14.addLayout(self.verticalLayout_18)

        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.pushButton_2 = QPushButton(self.frame_11)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(120, 35))
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_26.addWidget(self.pushButton_2)

        self.comboBox = QComboBox(self.frame_11)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(120, 35))

        self.verticalLayout_26.addWidget(self.comboBox)

        self.Com_Open_file = QPushButton(self.frame_11)
        self.Com_Open_file.setObjectName(u"Com_Open_file")
        self.Com_Open_file.setMinimumSize(QSize(120, 35))
        self.Com_Open_file.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_26.addWidget(self.Com_Open_file)


        self.horizontalLayout_14.addLayout(self.verticalLayout_26)


        self.verticalLayout_28.addLayout(self.horizontalLayout_14)

        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.Com_isOpenOrNot_Label = QLabel(self.frame_11)
        self.Com_isOpenOrNot_Label.setObjectName(u"Com_isOpenOrNot_Label")
        self.Com_isOpenOrNot_Label.setMinimumSize(QSize(0, 35))
        self.Com_isOpenOrNot_Label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.Com_isOpenOrNot_Label)

        self.Com_file_line = QLineEdit(self.frame_11)
        self.Com_file_line.setObjectName(u"Com_file_line")
        self.Com_file_line.setMinimumSize(QSize(0, 35))

        self.verticalLayout_27.addWidget(self.Com_file_line)

        self.progressBar = QProgressBar(self.frame_11)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(0, 35))
        self.progressBar.setLayoutDirection(Qt.LeftToRight)
        self.progressBar.setValue(24)
        self.progressBar.setOrientation(Qt.Horizontal)
        self.progressBar.setTextDirection(QProgressBar.TopToBottom)

        self.verticalLayout_27.addWidget(self.progressBar)


        self.verticalLayout_28.addLayout(self.verticalLayout_27)


        self.verticalLayout_33.addLayout(self.verticalLayout_28)


        self.horizontalLayout_26.addWidget(self.frame_11)


        self.verticalLayout_30.addLayout(self.horizontalLayout_26)

        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(610, 106))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_4)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.Command_select = QComboBox(self.frame_4)
        self.Command_select.addItem("")
        self.Command_select.addItem("")
        self.Command_select.setObjectName(u"Command_select")
        self.Command_select.setMinimumSize(QSize(0, 35))

        self.verticalLayout_29.addWidget(self.Command_select)

        self.lineEdit_3 = QLineEdit(self.frame_4)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(0, 35))

        self.verticalLayout_29.addWidget(self.lineEdit_3)


        self.verticalLayout_31.addWidget(self.frame_4)

        self.verticalSpacer_2 = QSpacerItem(20, 118, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_31.addItem(self.verticalSpacer_2)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(630, 160))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_3)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(120, 35))
        self.label_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.label_7)

        self.horizontalSpacer = QSpacerItem(208, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer)

        self.hexSending_checkBox = QCheckBox(self.frame_3)
        self.hexSending_checkBox.setObjectName(u"hexSending_checkBox")
        sizePolicy5.setHeightForWidth(self.hexSending_checkBox.sizePolicy().hasHeightForWidth())
        self.hexSending_checkBox.setSizePolicy(sizePolicy5)

        self.horizontalLayout_11.addWidget(self.hexSending_checkBox)

        self.Send_Button = QPushButton(self.frame_3)
        self.Send_Button.setObjectName(u"Send_Button")
        self.Send_Button.setMinimumSize(QSize(120, 35))

        self.horizontalLayout_11.addWidget(self.Send_Button)


        self.verticalLayout_32.addLayout(self.horizontalLayout_11)

        self.textEdit_Send = QTextEdit(self.frame_3)
        self.textEdit_Send.setObjectName(u"textEdit_Send")
        sizePolicy3.setHeightForWidth(self.textEdit_Send.sizePolicy().hasHeightForWidth())
        self.textEdit_Send.setSizePolicy(sizePolicy3)
        self.textEdit_Send.setMinimumSize(QSize(520, 100))
        self.textEdit_Send.setStyleSheet(u"QTextEdit#textEdit_Send{\n"
"	border-radius: 20px;\n"
"	border: 1px solid black;\n"
"	background-color: rgb(241, 241, 241);\n"
"}")

        self.verticalLayout_32.addWidget(self.textEdit_Send)


        self.verticalLayout_31.addWidget(self.frame_3)


        self.verticalLayout_30.addLayout(self.verticalLayout_31)


        self.horizontalLayout_27.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.ota)
        self.Real_time_charts = QWidget()
        self.Real_time_charts.setObjectName(u"Real_time_charts")
        self.verticalLayout_36 = QVBoxLayout(self.Real_time_charts)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.Real_time_charts)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_13)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.Chart_line = QLineEdit(self.frame_13)
        self.Chart_line.setObjectName(u"Chart_line")
        self.Chart_line.setMinimumSize(QSize(1020, 35))

        self.horizontalLayout_28.addWidget(self.Chart_line)

        self.Chart_btn = QPushButton(self.frame_13)
        self.Chart_btn.setObjectName(u"Chart_btn")
        self.Chart_btn.setMinimumSize(QSize(110, 35))
        self.Chart_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_28.addWidget(self.Chart_btn)


        self.verticalLayout_25.addLayout(self.horizontalLayout_28)

        self.Chart_widget = QWidget(self.frame_13)
        self.Chart_widget.setObjectName(u"Chart_widget")
        self.Chart_widget.setMinimumSize(QSize(1140, 650))
        self.Chart_widget.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_25.addWidget(self.Chart_widget)


        self.verticalLayout_35.addLayout(self.verticalLayout_25)


        self.verticalLayout_36.addWidget(self.frame_13)

        self.stackedWidget.addWidget(self.Real_time_charts)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        self.creditsLabel.setFont(font4)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.horizontalLayout_12.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"\u8f6f\u4ef6\u53ca\u6574\u673a", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>R&amp;DC-SCG-TOOL</p></body></html>", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"\u4e3b\u8981\u529f\u80fd", None))
        self.btn_widgets.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u56fe\u8868", None))
        self.btn_ota.setText(QCoreApplication.translate("MainWindow", u"OTA", None))
        self.btn_document.setText(QCoreApplication.translate("MainWindow", u"\u6587\u6863", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"style", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_share.setText(QCoreApplication.translate("MainWindow", u"Share", None))
        self.btn_adjustments.setText(QCoreApplication.translate("MainWindow", u"Adjustments", None))
        self.btn_more.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'\u5fae\u8f6f\u96c5\u9ed1'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:12pt; color:#ff00ff;\">\u5de5\u5177\u9002\u7528\u8303\u56f4</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:10pt;\">\u9002\u7528\u4e8e\u8f6f\u4ef6\u53ca\u6574\u673a\u6d4b\u8bd5</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\""
                        "><span style=\" font-family:'Segoe UI'; font-size:10pt;\">\u5904\u7406\u5145\u7535\u65f6\u957f\u3001\u7b5b\u9009\u6570\u636e</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:10pt;\">\u7b5b\u9009\u5e76\u751f\u6210\u66f2\u7ebf\u56fe</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:12pt; color:#ff55ff;\">\u5176\u4ed6\u529f\u80fd</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:9pt; color:#ff55ff;\">By\uff1aAn--\u53ef\u4ee5\u65b0\u589e\u529f\u80fd</span></p></body></html>", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"RDC-\u7814\u53d1\u90e8-\u6d4b\u8bd5\u7ec4-\u6570\u636e\u5904\u7406\u5de5\u5177", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.textEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u5c55\u793a", None))
        self.label_15.setText("")
        self.info_text.setText(QCoreApplication.translate("MainWindow", u"Info", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58 \u8def\u5f84", None))
#if QT_CONFIG(tooltip)
        self.line_filename.setToolTip(QCoreApplication.translate("MainWindow", u"\u591a\u4e2a\u8def\u5f84\u7684\u60c5\u51b5\u4e0b\u6ce8\u610f\u91cd\u65b0\u547d\u540d\u6587\u4ef6", None))
#endif // QT_CONFIG(tooltip)
        self.line_filename.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u9ed8\u8ba4\u5de5\u5177\u653e\u7f6e\u8def\u5f84\u4e0b\u7684data.csv", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6 \u8def\u5f84", None))
        self.line_filepath.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u9700\u8981\u6253\u5f00\u7684\u6570\u636e\u6587\u4ef6", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u6761\u4ef61", None))
#if QT_CONFIG(tooltip)
        self.line_data1.setToolTip(QCoreApplication.translate("MainWindow", u"\u6ce8\u610f\u4e0d\u8981<>", None))
#endif // QT_CONFIG(tooltip)
        self.line_data1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"motor", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u6761\u4ef62", None))
#if QT_CONFIG(tooltip)
        self.line_data2.setToolTip(QCoreApplication.translate("MainWindow", u"\u6ce8\u610f\u4e0d\u8981<>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.line_data2.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.line_data2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"imu", None))
        self.btn_get.setText(QCoreApplication.translate("MainWindow", u"\u83b7\u53d6\u6587\u4ef6\u8def\u5f84", None))
        self.btn_get_all_data.setText(QCoreApplication.translate("MainWindow", u"\u83b7\u53d6\u6570\u636e", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u5176\u4ed6\u529f\u80fd\u53c2\u7167\u4e0a\u8ff0\u7b5b\u67e5", None))
#if QT_CONFIG(tooltip)
        self.btn_chang_jump.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>info\u7684\u8df3\u7535\u60c5\u51b5</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_chang_jump.setText(QCoreApplication.translate("MainWindow", u"Info\u7535\u91cf", None))
#if QT_CONFIG(tooltip)
        self.btn_bat_jump.setToolTip(QCoreApplication.translate("MainWindow", u"bat\u547d\u4ee4\u7535\u91cf\u8df3\u7535\u60c5\u51b5", None))
#endif // QT_CONFIG(tooltip)
        self.btn_bat_jump.setText(QCoreApplication.translate("MainWindow", u"bat\u7535\u91cf", None))
#if QT_CONFIG(tooltip)
        self.btn_time.setToolTip(QCoreApplication.translate("MainWindow", u"info\u5145\u653e\u7535\u65f6\u957f", None))
#endif // QT_CONFIG(tooltip)
        self.btn_time.setText(QCoreApplication.translate("MainWindow", u"\u5145\u653e\u7535\u65f6\u957f", None))
#if QT_CONFIG(tooltip)
        self.btn_error.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>info\u544a\u8b66<br/>wip\u3001wop\u7b49</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_error.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u67e5\u544a\u8b66", None))
#if QT_CONFIG(tooltip)
        self.btn_status.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u5145\u7535\u72b6\u6001\u68c0\u6d4b</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_status.setText(QCoreApplication.translate("MainWindow", u"\u5145\u7535\u72b6\u6001", None))
        self.btn_dazhaun.setText(QCoreApplication.translate("MainWindow", u"\u8def\u5f84\u6253\u8f6c", None))
        self.start_vol_cur.setText(QCoreApplication.translate("MainWindow", u"Start-Ent\u53c2\u6570", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u7535\u538b\u7a33\u5b9a\u6027", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"\u7535\u6d41\u7a33\u5b9a\u6027", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"PATH", None))
        self.btn_open_csv.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.btn_create_image.setText(QCoreApplication.translate("MainWindow", u"\u751f\u6210", None))
        self.btn_clear_image.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u63a5\u6536\u7aef", None))
        self.hexShowing_checkBox.setText(QCoreApplication.translate("MainWindow", u"16\u8fdb\u5236", None))
        self.ClearButton.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664", None))
        self.Com_Refresh_Label.setText(QCoreApplication.translate("MainWindow", u"\u4e32\u53e3\u641c\u7d22", None))
        self.Com_Baud_Label.setText(QCoreApplication.translate("MainWindow", u"\u6ce2\u7279\u7387", None))
        self.Com_Name_Label.setText(QCoreApplication.translate("MainWindow", u"\u4e32\u53e3\u9009\u62e9", None))
        self.Com_Open_Label.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u4e32\u53e3", None))
        self.Com_Close_Label.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed\u4e32\u53e3", None))
        self.Com_Refresh_Button.setText(QCoreApplication.translate("MainWindow", u"\u5237\u65b0", None))
        self.Com_Baud_Combo.setItemText(0, QCoreApplication.translate("MainWindow", u"1200", None))
        self.Com_Baud_Combo.setItemText(1, QCoreApplication.translate("MainWindow", u"9600", None))
        self.Com_Baud_Combo.setItemText(2, QCoreApplication.translate("MainWindow", u"14400", None))
        self.Com_Baud_Combo.setItemText(3, QCoreApplication.translate("MainWindow", u"19200", None))
        self.Com_Baud_Combo.setItemText(4, QCoreApplication.translate("MainWindow", u"38400", None))
        self.Com_Baud_Combo.setItemText(5, QCoreApplication.translate("MainWindow", u"57600", None))
        self.Com_Baud_Combo.setItemText(6, QCoreApplication.translate("MainWindow", u"115200", None))
        self.Com_Baud_Combo.setItemText(7, QCoreApplication.translate("MainWindow", u"230400", None))

        self.Com_Open_Button.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.Com_Close_Button.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u5347\u7ea7", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u901f\u7387", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u8def\u5f84", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u5347\u7ea7", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"128", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"1024", None))

        self.Com_Open_file.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u6587\u4ef6", None))
        self.Com_isOpenOrNot_Label.setText(QCoreApplication.translate("MainWindow", u"\u4e32\u53e3\u5f85\u6253\u5f00", None))
        self.Command_select.setItemText(0, QCoreApplication.translate("MainWindow", u"motor", None))
        self.Command_select.setItemText(1, QCoreApplication.translate("MainWindow", u"meas", None))

        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u547d\u4ee4\u53c2\u6570", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001\u7aef", None))
        self.hexSending_checkBox.setText(QCoreApplication.translate("MainWindow", u"16\u8fdb\u5236", None))
        self.Send_Button.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001", None))
        self.Chart_btn.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001", None))
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By: Qing An", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"V1.11", None))
    # retranslateUi

