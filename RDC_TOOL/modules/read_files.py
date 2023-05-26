# -*- coding: utf-8 -*-
# https://blog.csdn.net/weixin_52040868
# 公众号：测个der
# 微信：qing_an_an


def with_open(path_name):
    with open(path_name, 'r', encoding='utf-8') as r:
        datas = r.read()
    return datas