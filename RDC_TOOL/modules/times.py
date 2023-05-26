# -*- coding: utf-8 -*-
# https://blog.csdn.net/weixin_52040868
# 公众号：测个der
# 微信：qing_an_an

import datetime

def data_times(value, stime, etime):
    if len(value) >= 12:
        start_time = datetime.datetime.strptime(stime, '%H:%M:%S.%f')
        end_time = datetime.datetime.strptime(etime, '%H:%M:%S.%f')
    else:
        start_time = datetime.datetime.strptime(stime, '%H:%M:%S')
        end_time = datetime.datetime.strptime(etime, '%H:%M:%S')
    over_time = end_time - start_time
    return str(over_time)
