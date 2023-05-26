# -*- coding: utf-8 -*-
# https://blog.csdn.net/weixin_52040868
# 公众号：测个der
# 微信：qing_an_an

# import pyqtgraph.examples
# pyqtgraph.examples.run()

# import re
import pyqtgraph as pg
from RDC_TOOL.main_functions import *
# from modules.times import data_times
from RDC_TOOL.modules import *

# def read(path):
#     with open(path, 'r', encoding='utf-8') as r:
#         datas = r.read()
#     return datas


def pg_plt(list_, txt):
    if list_:
        plt = pg.plot(list_, pen='r')
        plt.setWindowTitle("跳电")
        plt.setTitle(txt)

        # 创建文本项
        text_item = pg.TextItem(anchor=(0.5, 1))
        # text_item.setPos(0, max(list_))
        plt.getPlotItem().setRange(yRange=[0, max(list_)])  # 限制因为鼠标变动导致的图形变形
        plt.addItem(text_item)

        # 鼠标移动事件处理函数
        def mouseMoved(evt):
            pos = evt  # 获取鼠标所在的数据点位置
            if plt.sceneBoundingRect().contains(pos):
                mousePoint = plt.plotItem.vb.mapSceneToView(pos)
                index = int(mousePoint.x())  # 获取数据点的索引
                if index > 0 and index < len(list_):
                    # 更新文本项内容
                    text_item.setText(f"x={index}\n y={list_[index]}", color=(0, 255, 0))
                    text_item.setPos(mousePoint.x(), mousePoint.y())
                    text_item.show()
                else:
                    text_item.hide()
            else:
                text_item.hide()

        # 连接鼠标移动事件
        plt.scene().sigMouseMoved.connect(mouseMoved)

        pg.exec()


def pg_bat(path):
    list_ = []
    time_list = []

    if path:
        datas = with_open(path)
        values = re.findall('\[.*].*cap:\s*.*', datas)
        for value in values:
            time_list.append(value[1:values[0].index(']')])
            list_.append(int(value[-2:]))
    try:
        over_time = data_times(time_list[0],time_list[0],time_list[-1])
        pg_plt(list_,f"bat跳电情况-耗时{over_time}")
    except IndexError as e:
        print("数据源不正确")


def info_batt(path):
    datas = with_open(path)
    values = re.findall('\[.*\].*cap\s*:\s*.*%', datas)
    bat_list = [re.match('.*cap\s*:\s*(.*?)%', value) for value in values]
    pg_plt([int(i.group(1)) for i in bat_list], "info跳电情况")


# info_batt(r"C:\Users\admin\Desktop\新电机充电时长.log")
# if __name__ == '__main__':
#     # ALL_DATA().warn_data(path_name=r'F:\0.log',data1='warn',data2='work event')
#     pg_bat(r"C:\Users\admin\Desktop\111111.log")