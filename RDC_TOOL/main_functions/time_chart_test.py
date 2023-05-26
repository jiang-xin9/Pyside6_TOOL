# -*- coding: utf-8 -*-
# https://blog.csdn.net/weixin_52040868
# 公众号：测个der
# 微信：qing_an_an

"""正确显示时间-曲线"""
# import datetime
# import pyqtgraph as pg
# from PySide6.QtCore import QDateTime
# from PySide6.QtWidgets import QVBoxLayout
# from pyqtgraph import DateAxisItem, PlotDataItem
#
#
# class DataPlotWidget():
#     def __init__(self, ui):
#         super().__init__()
#         self.ui = ui
#         # 创建布局
#         self.layout = QVBoxLayout()
#         self.ui.Chart_widget.setLayout(self.layout)
#
#         # 创建GraphicsLayoutWidget作为容器
#         self.container = pg.GraphicsLayoutWidget()
#
#         # 将容器添加到布局中
#         self.layout.addWidget(self.container)
#
#         # 创建绘图窗口
#         self.win = self.container.addPlot()
#
#         # 设置时间轴
#         axis = pg.AxisItem(orientation='bottom')
#         axis.setLabel(text='Time', units='s')
#
#         # 创建一个X轴的时间轴类型
#         self.date_axis = DateAxisItem(orientation='bottom')
#         self.date_axis.setLabel(text='Time', units='s')
#         self.win.setAxisItems({'bottom': self.date_axis})
#
#         # 创建一个X轴的时间轴类型
#         # self.date_axis = pg.DateAxisItem(orientation='bottom',
#         #                                  format="%H:%M:%S.%f")  # Set the format for displaying time with milliseconds
#         # self.win.setAxisItems({'bottom': self.date_axis})
#
#         # 生成示例数据
#         self.timestamps = []
#         self.data = []
#
#         # 创建图形对象
#         # self.plot = self.win.plot()
#         self.plot = PlotDataItem()
#         self.win.addItem(self.plot)
#
#     def update_data(self, value):
#         # 生成当前时间戳和随机整数数据
#         # timestamp = datetime.datetime.now()
#         timestamp = datetime.datetime.now().timestamp()
#
#         print(value)
#         # 将数据添加到列表
#         self.timestamps.append(timestamp)
#         self.data.append(float(value))
#
#         # 更新图形数据
#         # self.plot.setData(x=[t.timestamp() for t in self.timestamps], y=self.data)
#         self.plot.setData(x=self.timestamps, y=self.data)
#         # self.plot.setData(x=[t.toMSecsSinceEpoch() for t in self.timestamps], y=self.data)
#
#         # 设置X轴范围为最后一分钟的数据
#         # xmin = (timestamp - datetime.timedelta(minutes=1)).timestamp()
#         # xmax = timestamp.timestamp()
#         # self.win.setXRange(xmin, xmax)
#         xmin = max(timestamp - 60, min(self.timestamps))
#         xmax = max(self.timestamps)
#         self.win.setXRange(xmin, xmax)



