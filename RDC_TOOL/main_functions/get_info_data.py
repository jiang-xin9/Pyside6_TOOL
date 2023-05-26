# -*- coding: utf-8 -*-
# https://blog.csdn.net/weixin_52040868
# 公众号：测个der
# 微信：qing_an_an


from RDC_TOOL.main_functions import *
from RDC_TOOL.modules.read_files import with_open

class RE_Data(object):

    def read_data(self,path_name, arg1, arg2, save_path):
        list_dic = []

        datas = with_open(path_name)
        # pattern = re.compile(r'<motor>(.*?)<imu>', re.DOTALL)
        pattern = re.compile(r'(?<={})([\s\S]*?)(?<={})'.format(arg1,arg2), re.DOTALL | re.IGNORECASE)
        # pattern = re.compile(r'(?<={})(?!{})([\s\S]*?)(?<={})'.format(re.escape(arg1), re.escape(arg1), re.escape(arg2)), re.DOTALL | re.IGNORECASE)
        if pattern:
            matches = pattern.findall(datas)
            for values in matches:
                pattern = re.compile(r'\[(.*)\](.*)\s+:\s*(.+?)(?=\s|$)')
            #     # 将数据字符串转换成字典
                my_dict = {}
                for line in values.split('\n'):
                    match = pattern.match(line)
                    if match:
                        key = match.group(2).strip()
                        values = match.group(3).strip()
                        my_dict[key] = values
                # print(my_dict)
                list_dic.append(my_dict)
            headers = [key for key in list_dic[0]]
            self.create_csv(save_path, headers, list_dic)

    def create_csv(self, path_name, headers, values):
        """
        :param path_name:  路径及名称
        :param title: 标题第一格头
        :return: csv file
        delimiter=','：使用逗号作为分隔符。
        quoting=csv.QUOTE_ALL：表示对所有元素都要加上引号，即使元素本身没有逗号也要加上引号。
        这是为了避免在特殊情况下，如元素中包含分隔符或引号时产生语法错误。
        """
        with open(path_name, 'w', newline='') as file:
            # for header in headers:
            writer = csv.DictWriter(file, fieldnames=headers, delimiter=',', quoting=csv.QUOTE_ALL)
            writer.writeheader()
            for value in values:
                try:
                    writer.writerow(value)
                except ValueError:
                    pass

# if __name__ == '__main__':
#     RE_Data().read_data(r'C:\Users\admin\Desktop\3系圆形泳池续航时长.log','batterry','motor','qq.csv')