import json
import time
import wifi
import socketpool
import ssl
import adafruit_requests
import sys
import microcontroller
import gc
import board
import analogio

try:
    analog_in = analogio.AnalogIn(board.IO7)
    networks = wifi.radio.start_scanning_networks()
    networks_sorted = sorted(networks, key=lambda net: net.rssi, reverse=True)
    for net in networks_sorted:
        print("SSID:", net.ssid, " Signal strength (RSSI):", net.rssi, "dBm")
        time.sleep(2)
    wifi.radio.connect("CMCC-z", "3bt")
    pool = socketpool.SocketPool(wifi.radio)
    ssl_context = ssl.create_default_context()
    session = adafruit_requests.Session(pool, ssl_context)
    a=0
    b=0
    for net in networks_sorted:
        url = 'https://a1.fanbook.mobi/api/bot/0f2de6abf3f1e202c5a06c2ae4a3f6cf94ab795fbfbe39ad311a18ad1ff314388d1c/sendMessage'
        headers = {'content-type':"application/json;charset=utf-8"}
        jsonfile=json.dumps({
            "chat_id":491517780416,
            "text": "SSID:"+ net.ssid+ " Signal strength (RSSI):"+ str(net.rssi)+ "dBm"
        })
        postreturn=session.post(url,data=jsonfile,headers=headers)
        print(postreturn.text)
    url = 'https://a1.fanbook.mobi/api/bot/406b93bf1e48f93a23f7791e0235e880749c252ce985779067b538b71cc69c08d/getGuildMembersCount'
    headers = {'content-type':"application/json;charset=utf-8"}
    jsonfile = json.dumps({"guild_id":43320445539664})
    postreturn = session.post(url, data=jsonfile, headers=headers)
    usershuliang1 = int(postreturn.json()['result'])
    print('1:' + str(usershuliang1))
    
    url = 'https://a1.fanbook.mobi/api/bot/406b933c545b8c16e654fbbf1e48f93a23f7791e0235e880749c252ce985779067b538b71cc69c08d/getGuildMembersCount'
    headers = {'content-type':"application/json;charset=utf-8"}
    jsonfile = json.dumps({"guild_id":451665184272})
    postreturn = session.post(url, data=jsonfile, headers=headers)
    ausershuliang1 = int(postreturn.json()['result'])
    print('J1:' + str(ausershuliang1))
        
    while True:
        iov=0
        a+=1
        b+=1
        time.sleep(1)
        url = 'https://a1.fanbook.mobi/api/bot/406b8c16e654fbbf1e48f93a23f7791e0235e880749c252ce985779067b538b71cc69c08d/getGuildMembersCount'
        headers = {'content-type':"application/json;charset=utf-8"}
        jsonfile = json.dumps({"guild_id":4332044553664})
        postreturn = session.post(url, data=jsonfile, headers=headers)
        usershuliang2 = int(postreturn.json()['result'])
        print('2:' + str(usershuliang2))
        
        url = 'https://a1.fanbook.mobi/api/bot/406b933bbf1e48f93a23f7791e0235e880749c252ce985779067b538b71cc69c08d/getGuildMembersCount'
        headers = {'content-type':"application/json;charset=utf-8"}
        jsonfile = json.dumps({"guild_id":45166518414272})
        postreturn = session.post(url, data=jsonfile, headers=headers)
        ausershuliang2 = int(postreturn.json()['result'])
        print('J2:' + str(ausershuliang2))
        if usershuliang1 < usershuliang2:
            print('texting')
            url = 'https://a1.fanbook.mobi/api/bot/406b9337d9f654fbbf1e48f93a23f7791e0235e880749c252ce985779067b538b71cc69c08d/sendPhoto'
            headers = {'content-type':"application/json;charset=utf-8"}
            jsonfile = json.dumps({
                "photo": {
                "Url": "https://29898903.s21i.faiusr.com/3/ABUIABADGAAgl9f8nAYorc3YpgMwwAI4tAE!1500x1500.gif.webp"
                },
                "chat_id":433204439
            })
            postreturn = session.post(url, data=jsonfile, headers=headers)
            url = 'https://a1.fanbook.mobi/api/bot/406b93e48f93a23f7791e0235e880749c252ce985779067b538b71cc69c08d/sendMessage'
            headers = {'content-type':"application/json;charset=utf-8"}
            jsonfile=json.dumps({
                "chat_id":433204479139,
                "text": "{\"type\":\"richText\",\"title\":\"欢迎第"+str(usershuliang2)+"位新成员加入！\",\"document\":\"[{\\\"insert\\\":\\\"欢迎加入\\\"}]\"}",
                "parse_mode": "Fanbook"
            })
            postreturn=session.post(url,data=jsonfile,headers=headers)
            print(postreturn.text)
            url = 'https://a1.fanbook.mobi/api/bot/406b9337d9ffab2be8f83dc535e880749c252ce985779067b538b71cc69c08d/getGuildMembersCount'
            headers = {'content-type':"application/json;charset=utf-8"}
            jsonfile = json.dumps({"guild_id":433204455396081664})
            postreturn = session.post(url, data=jsonfile, headers=headers)
            usershuliang1 = int(postreturn.json()['result'])
            print('1:' + str(usershuliang1))
        if ausershuliang1 < ausershuliang2:
            print('texting')
            url = 'https://a1.fanbook.mobi/api/bot/406b9337d9ffab2be8f83dc5450235e880749c252ce985779067b538b71cc69c08d/sendMessage'
            headers = {'content-type':"application/json;charset=utf-8"}
            jsonfile=json.dumps({
                "chat_id":480566392,
                "text": "{\"type\":\"richText\",\"title\":\"欢迎第"+str(ausershuliang2)+"位新成员加入！\",\"document\":\"[{\\\"insert\\\":\\\"欢迎加入\\\"}]\"}",
                "parse_mode": "Fanbook"
            })
            postreturn=session.post(url,data=jsonfile,headers=headers)
            print(postreturn.text)
            url = 'https://a1.fanbook.mobi/api/bot/406b9337791e0235e880749c252ce985779067b538b71cc69c08d/getGuildMembersCount'
            headers = {'content-type':"application/json;charset=utf-8"}
            jsonfile = json.dumps({"guild_id":4516272})
            postreturn = session.post(url, data=jsonfile, headers=headers)
            ausershuliang1 = int(postreturn.json()['result'])
            print('J1:' + str(ausershuliang1))
        if a==30:
            sys.stdout.write("\033[2J\033[;H")
            a=0
            temp = microcontroller.cpu.temperature
            print("Temperature: {:.2f}C".format(temp))
            free_mem = gc.mem_free()
            alloc_mem = gc.mem_alloc()
            for i in range(10):
                voltage = analog_in.value
                iov+=voltage
            iov1=iov//10
            print("Free memory: {} bytes, Allocated memory: {} bytes".format(free_mem, alloc_mem))
            gc.collect()
            url = 'https://a1.fanbook.mobi/api/bot/0f2de7ac66727cd3f1e202c5a06c2ae4a3f6cf94ab795fbfbe39ad311a18ad1ff314388d1c/sendMessage'
            headers = {'content-type':"application/json;charset=utf-8"}
            jsonfile=json.dumps({
                "chat_id":491517780416,
                "text": "CPU温度:"+str(temp)+" ℃"+",可用内存："+str(free_mem)+" bytes,已分配内存"+str(alloc_mem)+" bytes,电压模拟值:"+str(iov1)
            })
            postreturn=session.post(url,data=jsonfile,headers=headers)
            print(postreturn.text)
        if b==550:
            microcontroller.reset()

except Exception as e:
    try:
        url = 'https://a1.fanbook.mobi/api/bot/0f2de7ac61e202c5a06c2ae4a3f6cf94ab795fbfbe39ad311a18ad1ff314388d1c/sendMessage'
        headers = {'content-type':"application/json;charset=utf-8"}
        jsonfile=json.dumps({
            "chat_id":4915172780416,
            "text": "error"
        })
        postreturn=session.post(url,data=jsonfile,headers=headers)
        print(postreturn.text)
    except Exception as e:
        microcontroller.reset()
    microcontroller.reset()
