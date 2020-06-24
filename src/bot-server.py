#-*-coding:utf-8-*-

import json
import asyncio
import discord
import time
from unicodeStringData import dbl2singleStr

with open("../secrets.json", "r") as secrets_json:
    secrets_json = json.load(secrets_json)
token = secrets_json["token"]

client = discord.Client()

# 봇이 구동된 이벤트
@client.event
async def on_ready():

    print("Logged in as")
    print("Bot Name:", client.user.name)
    print("Bot ID:", client.user.id)
    
    # discord activity 기능을 활용하여, 상태 표시
    activity = discord.Game(name="여러분의 말을 기억")
    await client.change_presence(status=discord.Status.idle, activity=activity)

# 봇이 새로운 메시지를 수신했을 때의 이벤트
@client.event
async def on_message(message):
    f = open("record.txt", 'a',  -1, "utf-16")
    
    if message.author.bot: #만약 메시지를 보낸사람이 봇일 경우
        return None
    
    #메시지를 보낸사람의 ID
    id = message.author.id 
    name = message.author.name
    # print(id)
    tm = time.localtime(time.time())
    timestring = time.strftime('%Y-%m-%d %I:%M:%S %p', tm)

    data = u"---------------\n"
    data += u"이름: {}\n".format(name)
    data += u"채널: {}\n".format(message.channel.name)
    data += u"내용: {}\n".format(dbl2singleStr(message.content))
    data += u"시간: {}\n".format(timestring)
    data += u"---------------\n"
    f.write(data)

    # channel = message.channel
    # if message.content.startswith('!채널설정'): 
    #     await channel.send('어디에 여러분의 채팅을 기록할까요?') 
    # else: 
    #     await channel.send("<@"+str(id)+">님이 \""+message.content+"\"라고 말하였습니다.")
    f.close()
client.run(token)