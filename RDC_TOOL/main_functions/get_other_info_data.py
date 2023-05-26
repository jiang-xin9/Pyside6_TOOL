# -*- coding: utf-8 -*-
# https://blog.csdn.net/weixin_52040868
# 公众号：测个der
# 微信：qing_an_an


from RDC_TOOL.main_functions import *
# import re
from RDC_TOOL.modules.times import data_times


class ALL_DATA:

    def read_data(self, path_name, args1='batterry', args2='motor'):
        with open(path_name, 'r', encoding='utf-8') as r:
            datas = r.read()
            matches = re.findall(r'<{}>(.*?)<{}>'.format(args1, args2), datas, re.DOTALL)
            return matches

    def get_info_battary_time(self, path_name, args1="charge", args2="warn"):
        """info充放电时长"""
        data_time = None

        matches = self.read_data(path_name)
        status = self.read_data(path_name, args1, args2)
        # 时长
        time_list = [re.search(r'\[(.*)\].*cap\s*:\s*(\d+)\s*%', cap).group(1) for cap in matches]
        # 状态
        status_list = [re.search(r'\[(.*)\].*status\s*:\s*(\w*)', sta).group(2) for sta in status]

        if "null" not in status_list[0]:
            return ['没有status: null数据']

        if status_list[0] == 'null':  # 放电
            data_time = "用时 {}".format(data_times(time_list[0], time_list[0], time_list[-1]))
        else:  # 充电
            for num, (value, stus) in enumerate(zip(time_list, status_list)):
                if stus == 'full':  # 充满
                    data_time = "用时 {}".format(data_times(time_list[0], time_list[0], value))
                    break
        print(data_time)
        return data_time

    def get_battary_jump(self, path_name):
        """info跳电情况"""
        battary_num = []
        time_list = []
        matches = self.read_data(path_name)
        for values in matches:
            pattern = re.compile(r'\[(.*)\].*cap\s*:\s*(\d+)\s*%')
            for line in values.split('\n'):
                match = pattern.match(line)
                if match:
                    battarys = match.group(2)
                    all_data = match.group()
                    time_ = match.group(1).strip()
                    battary_num.append([all_data, battarys])
                    time_list.append(time_)

        jump_list_ = []
        try:
            if int(battary_num[0][1]) >= 50:

                for value, num in zip(battary_num, range(len(battary_num) - 1)):
                    # 第一个减去第二个...放电
                    jump_barrary = int(battary_num[num][1]) - int(battary_num[num + 1][1])
                    if jump_barrary == 0:
                        continue
                    if jump_barrary < 0:
                        jump_list_.append(f"{battary_num[num][0]} 电量上升：{str(jump_barrary)[1:]}" + '%')
                    if jump_barrary > 1:
                        jump_list_.append(f"{battary_num[num][0]} 电量下降：{str(jump_barrary)}" + "%")
            else:
                for value, num in zip(battary_num, range(len(battary_num) - 1)):
                    # 第二个减去第一个...充电
                    jump_barrary = int(battary_num[num + 1][1]) - int(battary_num[num][1])
                    if jump_barrary == 0:
                        continue
                    if jump_barrary < 0:
                        jump_list_.append(f"{battary_num[num + 1][0]} 电量下降：{str(jump_barrary)[1:]}" + '%')
                    if jump_barrary > 1:
                        jump_list_.append(f"{battary_num[num + 1][0]} 电量上升：{str(jump_barrary)}" + "%")
        except IndexError as e:
            return [f"{e}，请检查日志数据，是否存在规定日志"]

        return jump_list_

    def get_bat_battery_data(self, path_name):
        """bat跳电"""
        list_ = []
        with open(path_name, 'r', encoding='utf-8') as r:
            datas = r.read()
            values = re.findall('\[.*].*cap:\s*.*', datas)
            try:
                if int(values[0][-2:]) >= 50:
                    """放电"""
                    for i in range(len(values) - 1):
                        if int(values[i][-2:]) - int(values[i + 1][-2:]) > 1:
                            data = "跳电 " + "前 " + values[i] + " 后 " + values[i + 1]
                            list_.append(data)
                        if int(values[i][-2:]) - int(values[i + 1][-2:]) < 0:
                            data = "回电 " + "前 " + values[i] + " 后 " + values[i + 1]
                            list_.append(data)
                else:
                    """充电"""
                    for i in range(len(values) - 1):
                        if int(values[i + 1][-2:]) - int(values[i][-2:]) > 1:
                            data = "跳电 " + "前 " + values[i] + " 后 " + values[i + 1]
                            list_.append(data)
                        if int(values[i + 1][-2:]) - int(values[i][-2:]) < 0:
                            data = "回电 " + "前 " + values[i] + " 后 " + values[i + 1]
                            list_.append(data)
            except IndexError as e:
                return [f"{e}，请检查日志数据，是否存在规定日志"]
        return list_

    def get_charge_data(self, path_name):
        """充电状态"""
        list_dic = []
        matches = self.read_data(path_name, 'charge', 'warn')
        for values in matches:
            lines = values.split('\n')
            # 创建一个空字典
            result = {}
            # 遍历每一行数据
            for line in lines:
                # 如果当前行包含'vol'、'cur'或'status'关键字
                if 'vol' in line or 'cur' in line or 'status' in line:
                    values = re.compile(r'\[(.*)](.*)\s*:\s*(.+?)(?=\s |$)')
                    match = values.match(line)
                    if match:
                        result[match.group(2).strip()] = match.group()
            # 判断充电charging
            if "charging" not in result['status']:
                list_dic.append(result)
        return list_dic

    def get_warn_data(self, path_name, data1, data2):
        """告警情况"""
        key_list = []
        value_list = []
        matches = self.read_data(path_name, data1, data2)
        for values in matches:
            pattern = re.compile(r'(\[(.*)].*\w*\s*):(\s*(\d+)\s*)')
            # 将数据字符串转换成字典
            for line in values.split('\n'):
                match = pattern.match(line)
                if match:
                    keys = match.group(1).strip()
                    values = match.group(3).strip()
                    key_list.append(keys)
                    value_list.append(values)
                # else:
                #     return ['没有告警']

        warn_list = []
        for key, value in zip(key_list, value_list):
            if value == '1':
                warn_ = key + ':' + value
                warn_list.append(warn_)
        return warn_list

if __name__ == '__main__':
    # ALL_DATA().warn_data(path_name=r'F:\0.log',data1='warn',data2='work event')
    ALL_DATA().get_info_battary_time(r"F:\1.log")
