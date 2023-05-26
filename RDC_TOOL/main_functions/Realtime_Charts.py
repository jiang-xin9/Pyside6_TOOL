# -*- coding: utf-8 -*-
# https://blog.csdn.net/weixin_52040868
# 公众号：测个der
# 微信：qing_an_an

import datetime
import pyqtgraph as pg
from PySide6.QtWidgets import QVBoxLayout
from pyqtgraph import DateAxisItem, PlotDataItem, AxisItem, PlotWidget


class TimeAxisItem(AxisItem):
    def __init__(self, orientation, *args, **kwargs):
        super().__init__(orientation, *args, **kwargs)

    def tickStrings(self, values, scale, spacing):
        return [datetime.datetime.fromtimestamp(value).strftime("%H:%M:%S.%f")[:-3] for value in values]


class DataPlotWidget():
    def __init__(self, ui):
        self.ui = ui
        # 创建布局
        self.layout = QVBoxLayout()
        self.ui.Chart_widget.setLayout(self.layout)

        # 创建绘图窗口
        self.plot_widget = PlotWidget()

        # 设置时间轴
        self.date_axis = TimeAxisItem(orientation='bottom')
        self.date_axis.setLabel(text='Time')
        self.plot_widget.getPlotItem().setAxisItems({'bottom': self.date_axis})

        # 生成示例数据
        self.timestamps = []
        self.data = []

        # 创建图形对象
        # 设置样式表
        pg.setConfigOptions(antialias=True)
        pg.setConfigOption('background', 'w')
        pg.setConfigOption('foreground', 'k')
        self.plot = PlotDataItem(pen=pg.mkPen(color='w', width=2))  # 设置曲线的样式
        self.plot_widget.addItem(self.plot)

        # 创建文本项
        self.text_item = pg.TextItem(anchor=(0, 1))
        self.plot_widget.addItem(self.text_item)
        self.text_item.hide()

        # 连接鼠标移动事件
        self.plot_widget.scene().sigMouseMoved.connect(self.mouseMoved)
        # 将绘图窗口添加到布局中
        self.layout.addWidget(self.plot_widget)

    def mouseMoved(self, evt):
        pos = self.plot_widget.mapFromScene(evt)
        if self.plot_widget.sceneBoundingRect().contains(pos):
            mousePoint = self.plot_widget.plotItem.vb.mapSceneToView(pos)
            index = self.find_nearest_index(mousePoint.x(), self.timestamps)
            if index is not None:
                x_val = datetime.datetime.fromtimestamp(self.timestamps[index]).strftime("%H:%M:%S.%f")[:-3]
                y_val = self.data[index]
                self.text_item.setText(f"x={x_val}\n y={y_val}", color=(0, 255, 0))
                self.text_item.setPos(mousePoint.x(), mousePoint.y())
                self.text_item.show()
        else:
            self.text_item.hide()

    @staticmethod
    def find_nearest_index(x, data):
        if len(data) == 0:
            return None
        idx = min(range(len(data)), key=lambda i: abs(data[i] - x))
        return idx

    def update_data(self, value):
        # 生成当前时间戳和随机整数数据
        timestamp = datetime.datetime.now().timestamp()

        # 将数据添加到列表
        self.timestamps.append(timestamp)
        self.data.append(float(value))

        # 更新图形数据
        self.plot.setData(x=self.timestamps, y=self.data)

        # 设置X轴范围为最后一分钟的数据
        xmin = max(timestamp - 60, min(self.timestamps))
        xmax = max(self.timestamps)
        self.plot_widget.setXRange(xmin, xmax)