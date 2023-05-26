# Pyside6_TOOL

#### 介绍
clone后运行main.py

UI框架二开。功能实现结合公司业务开发。基于Pyside6开发的数据处理工具兼上位机工具，读取CSV数据作图，实时数据曲线图，OTA升级，串口通信调试。

主要业务逻辑在main_functions中写的。

转换命令("如果有更新，切换到RDC..目录下控制台输入，然后替换掉原有的")

pyside6-rcc resources.qrc -o resources_rc.py

pyside6-uic main.ui -o ui_main.py

打包：

Pyinstaller -F -w -i images\images\icon.ico --name="数据处理工具兼上位机V1.11" main.py

[使用视频](https://www.aliyundrive.com/s/gdUTA28A5xb)

#### 模块版本说明
python                    3.95

pandas                    2.0.1

pyinstaller               5.11.0

pyinstaller-hooks-contrib 2023.3

pyserial                  3.5

pyqtgraph                 0.13.3

PySide6                   6.5.0

PySide6-Addons            6.5.0

PySide6-Essentials        6.5.0

#### 安装教程

1.  pip install pyside6

其他缺少模块同理，下载慢就换镜像

#### 使用说明
第一个界面是根据公司业务，日志情况写的，主要用于筛选日志存储CSV文件。

1.  此界面会根据CSV第一行加载，会自动加载到combox中，选择生成对应的数据即可，最多支持加载两个数据图

![CSV图表加载](https://foruda.gitee.com/images/1685095324067247170/a6bad614_9752931.png "企业微信截图_16850952855663.png")

2.  此界面在线调试，OTA升级，默认保存日志文件。

![OTA-DBUG](https://foruda.gitee.com/images/1685095497097890061/d47b47d9_9752931.png "企业微信截图_16850954623405.png")

3.  此界面是实时数据加载，re规则默认匹配“数字”，例如open:12.2。会自动将12.2加载到图标中。X轴时间戳是当前时间，时分秒毫秒。支持鼠标移动加载XY轴对应的数值。

![实时数据](https://foruda.gitee.com/images/1685095597792166721/7a19db71_9752931.png "企业微信截图_16850955693569.png")

#### 参与贡献

1.  作者：清安无别事
2.  微信：qing_an_an
