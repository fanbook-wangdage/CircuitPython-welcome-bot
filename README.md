# CircuitPython-welcome-bot
fanbook CircuitPython welcome bot  
# 利用带网络功能的CircuitPython开发板创建欢迎机器人  
开发板需支持CircuitPython，并且可联网，代码及库存储空间需要大于3.55MB  
本示例开发板：hiibot_iots2_v2（CircuitPython 7.0.0）(约40元)  
[点击加入问题反馈服务器](https://fanbook.mobi/LmgLJF3N "点击加入问题反馈服务器")  
# 使用教程：  
1.另存所有开发板附带文件，并删除所有开发板内自带文件（除boot_out.txt）  
2.解压这里的lib(库文件夹)复制到开发板根目录  
3.自己存一份这里的code.py，使用文本编辑器或者代码编辑器打开  
4.修改以下代码中的**中文提示部分**：  
20行：
```python
wifi.radio.connect("无线网络名称", "网络密码")
```  
27行：  
```python
url = 'https://a1.fanbook.mobi/api/bot/需要发送日志的机器人令牌/sendMessage'
```  
30行：  
```python
            "chat_id":需要发送日志的频道id,#(填错不会发送，不会导致问题，但是不填会报错)
```
35行：  
```python
    url = 'https://a1.fanbook.mobi/api/bot/欢迎机器人令牌/getGuildMembersCount'
```
37行：  
```python
    jsonfile = json.dumps({"guild_id":服务器id})
```  
**其他类似行也需要修改**
**第42、44修改方式同35、37行（服务器id和机器人令牌使用第二个服务器的）**  
**代码默认支持两个服务器，如果只有一个服务器，删除42到48行，61行到66行，93行到109行**  
遇到例如54行、56行这样的内容，把链接中令牌的位置换为自己机器人的令牌，guild_id冒号后跟服务器id，chat_id冒号后跟频道id，73行的"Url"冒号后跟**欢迎时发送的图片链接**，不需要可删除第85行  
![示例图片](https://fanbookwdg3.bailituya.com/i/2023/05/07/pczrkt.png)   
**110行后的频道id全部为日志频道id，遇到错误会重启**  
还有什么问题吗？  
[点击加入问题反馈服务器](https://fanbook.mobi/LmgLJF3N "点击加入问题反馈服务器")  
