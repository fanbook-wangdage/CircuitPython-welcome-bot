# CircuitPython-welcome-bot
fanbook CircuitPython welcome bot  
# 利用带网络功能的CircuitPython开发板创建欢迎机器人  
开发板需支持CircuitPython，并且可联网，代码及库存储空间需要大于3.55MB  
本示例开发板：hiibot_iots2_v2（CircuitPython 7.0.0）(约40元)  
# 使用教程：  
1.另存所有开发板附带文件，并删除所有开发板内自带文件  
2.复制lib(库文件夹)到根目录  
3.自己存一份这里的code.py，使用文本编辑器或者代码编辑器打开  
4.修改以下代码：  
20行：  
''
    wifi.radio.connect("无线网络名称", "网络密码")
''  
27行：  
''
        url = 'https://a1.fanbook.mobi/api/bot/需要发送日志的机器人令牌/sendMessage'
'' 
