# -*- coding: utf-8 -*-
# https://blog.csdn.net/weixin_52040868
# 公众号：测个der
# 微信：qing_an_an

import time
import pandas as pd
from datetime import datetime, date
from RDC_TOOL.modules import *
from PySide6.QtGui import QWheelEvent
from PySide6.QtCore import QThread, Signal


# 获取具体数据
class Csv_datas_Thread(QThread):
    # 自定义信号，用于在线程中发送消息
    update_signal = Signal(pd.DataFrame)

    def __init__(self, path, text,text1 = None):
        super().__init__()
        self.path = path
        self.text = text
        self.text1 = text1

    def run(self) -> None:
        datas = pd.read_csv(self.path, encoding='utf-8')
        if self.text1 is not None:
            self.update_signal.emit(datas[[self.text, self.text1]])
        else:
            self.update_signal.emit(datas[self.text])



# 自动获取下拉列表的值
class Csv_header_Thread(QThread):
    # 自定义信号，用于在线程中发送消息
    update_signal = Signal(list)

    def __init__(self,path):
        super().__init__()
        self.path = path

    def run(self):
        if self.path:
            csv_datas = pd.read_csv(self.path, encoding='utf-8')
            header = csv_datas.columns.tolist()
            self.update_signal.emit(header)

class ChartData:
    def __init__(self):
        self.chart_view = None
        self.series = None
        self.series1 = None
        self.axis_y1 = None

    def update_chart(self, win, title, datas, title1=None, datas1=None):
        if self.chart_view is None:
            self.create_chart_view(win)

        self.clear_chart()  # 清除之前的数据系列
        self.create_chart(title, datas, title1, datas1)  # 生成新的曲线图

    def create_chart_view(self, win):
        chart_widget = win
        layout = QVBoxLayout(chart_widget)
        layout.setContentsMargins(0, 0, 0, 0)

        self.chart_view = QChartView(chart_widget)
        self.chart_view.setRenderHint(QPainter.Antialiasing)    # 抗锯齿
        self.chart_view.setRubberBand(QChartView.RectangleRubberBand)   # 选择区域放大
        self.chart_view.setDragMode(QChartView.ScrollHandDrag)  # 设置拖拽模式
        self.chart_view.setInteractive(True)    # 开启交互模式
        self.chart_view.chart().setTheme(QChart.ChartThemeBlueCerulean)  # 设置主题
        self.chart_view.chart().setDropShadowEnabled(True)  # 阴影
        self.chart_view.chart().setAnimationOptions(QChart.AllAnimations)  # 动画效果
        self.chart_view.chart().createDefaultAxes()  # 创建默认坐标轴

        target_size = chart_widget.size()
        self.chart_view.setMinimumSize(target_size.width(), target_size.height())

        layout.addWidget(self.chart_view)

    def create_chart(self, title, datas, title1=None, datas1=None):
        chart = QChart()
        chart.removeAllSeries()

        chart.setTitle('数据曲线图')
        chart.setTheme(QChart.ChartThemeBlueCerulean)
        chart.setDropShadowEnabled(True)
        chart.setAnimationOptions(QChart.AllAnimations)
        chart.createDefaultAxes()

        self.series = QLineSeries()
        self.series.setName(title + "数据")
        font = QFont("Arial", 13, QFont.Bold)
        chart.setTitleFont(font)

        for i, j in enumerate(datas):
            self.series.append(i, j)

        if datas1 is not None:
            self.series1 = QLineSeries()
            self.series1.setName(title1 + "数据")

            self.axis_y1 = QValueAxis()
            self.axis_y1.setMin(0)
            self.axis_y1.setLabelFormat("%d")
            self.axis_y1.setTickCount(6)
            chart.addAxis(self.axis_y1, Qt.AlignRight)
            self.series1.attachAxis(self.axis_y1)

            for k, v in enumerate(datas1):
                self.series1.append(k, v)

            chart.addSeries(self.series1)

        chart.addSeries(self.series)

        axis_x = QValueAxis()
        axis_x.setLabelFormat("%d")
        axis_x.setTitleText('行 数 端')
        axis_x.setTickCount(6)
        chart.setAxisX(axis_x, self.series)

        axis_y = QValueAxis()
        axis_y.setMin(0)
        axis_y.setLabelFormat("%d")
        axis_y.setTitleText("数 据 端")
        axis_y.setTickCount(6)
        chart.addAxis(axis_y, Qt.AlignLeft)
        self.series.attachAxis(axis_y)

        # 鼠标滚轮事件
        def wheelEvent(event: QWheelEvent):
            factor = 1.2  # Scaling factor
            pos = self.chart_view.mapToScene(self.chart_view.mapFromGlobal(QCursor.pos()))  # Get the mouse position
            delta = event.angleDelta().y()  # Get the scrolling distance

            chart_rect = self.chart_view.chart().plotArea()
            width = chart_rect.width()
            center = chart_rect.center()

            if delta > 0:
                chart_rect.setWidth(width / factor)  # Zoom in by adjusting the width
            else:
                chart_rect.setWidth(width * factor)  # Zoom out by adjusting the width

            chart_rect.moveCenter(center)
            self.chart_view.chart().zoomIn(chart_rect)  # Zoom in/out using the updated plot area

            event.accept()

        self.chart_view.wheelEvent = wheelEvent

        self.chart_view.setChart(chart)

    def clear_chart(self):  # 清除绘图
        if self.chart_view is not None:
            chart = self.chart_view.chart()

            if self.series is not None:
                chart.removeSeries(self.series)
                self.series = None

            if self.series1 is not None:
                chart.removeSeries(self.series1)
                self.series1 = None

            if self.axis_y1 is not None:
                chart.removeAxis(self.axis_y1)
                self.axis_y1 = None

"""以下是X轴添加时间模块，必须要年月日时分秒毫秒"""
# import sys
# from PySide6.QtCore import QDateTime, Qt, QPointF
# from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
# from PySide6 import QtCharts
# from matploat import pg_bat
# import time
# from datetime import datetime, date
#
#
# # 获取当前日期
# current_date = date.today()
# bat = pg_bat(r"C:\Users\admin\Desktop\2023_05_18_Serial-COM3_21_51.log")
# timestamps = []
# for time_ in bat[1]:
#     datetime_str = f"{current_date} {time_}"
#     dt = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S.%f")
#     timestamp = int(dt.timestamp() * 1000) + int(dt.microsecond / 1000)
#     timestamps.append(timestamp)
# values = bat[0]
#
# app = QApplication(sys.argv)
#
# # 创建主窗口和布局
# window = QMainWindow()
# window_layout = QVBoxLayout()
# central_widget = QWidget()
#
# # 创建图表和图表视图
# chart = QtCharts.QChart()
# chart_view = QtCharts.QChartView(chart)
#
# # 创建折线图数据系列
# series = QtCharts.QLineSeries()
#
# # 添加数据到折线图数据系列
# for i in range(len(timestamps)):
#     timestamp = timestamps[i]
#     value = values[i]
#     qdatetime = QDateTime.fromMSecsSinceEpoch(timestamp)
#     point = QPointF(float(qdatetime.toMSecsSinceEpoch()), value)
#     series.append(point)
#
# # 将折线图数据系列添加到图表
# chart.addSeries(series)
#
# # 创建 Y 轴
# axis_y = QtCharts.QValueAxis()
# axis_y.setRange(min(values), max(values))
# axis_y.setLabelFormat("%.2f")
# chart.addAxis(axis_y, Qt.AlignLeft)
# series.attachAxis(axis_y)
#
# # 创建 X 轴
# axis_x = QtCharts.QDateTimeAxis()
# axis_x.setTickCount(8)
# axis_x.setFormat("hh:mm:ss")
#
# axis_x.setMin(QDateTime.fromMSecsSinceEpoch(timestamps[0]))  # 设置 X 轴的起始值为第一个时间戳
# axis_x.setMax(QDateTime.fromMSecsSinceEpoch(timestamps[-1]))  # 设置 X 轴的末尾值为最后一个时间戳
# chart.addAxis(axis_x, Qt.AlignBottom)
# series.attachAxis(axis_x)
#
# # 设置图表标题和图例
# chart.setTitle("My Chart")
# chart.legend().setVisible(True)
#
# # 将图表视图添加到布局
# window_layout.addWidget(chart_view)
#
# # 设置布局到主窗口的中央部件
# central_widget.setLayout(window_layout)
# window.setCentralWidget(central_widget)
#
# # 显示窗口
# window.show()
#
# # 运行应用程序的事件循环
# sys.exit(app.exec())
