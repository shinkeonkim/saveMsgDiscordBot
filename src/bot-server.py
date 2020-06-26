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
    with open("../data/record.json", "r", encoding="utf-8") as records:
        records = json.load(records)
    
    msg_list = records["msg_list"]
    print(msg_list)
    
    if message.author.bot: #만약 메시지를 보낸사람이 봇일 경우
        return None
    
    #메시지를 보낸사람의 ID
    id = message.author.id 
    name = message.author.name
    tm = time.localtime(time.time())
    timestring = time.strftime('%Y-%m-%d %I:%M:%S %p', tm)

    data  = {}
    data["이름"] = dbl2singleStr(name)
    data["채널"] = dbl2singleStr(message.channel.name)
    data["내용"] = dbl2singleStr(message.content)
    data["시간"] = dbl2singleStr(timestring)
    msg_list.append(data)

    json_dict = {"msg_list":msg_list}
    
    with open("../data/record.json", "w", encoding="utf-8") as records:
        json.dump(json_dict, records)

    # channel = message.channel
    # if message.content.startswith('!채널설정'): 
    #     await channel.send('어디에 여러분의 채팅을 기록할까요?') 
    # else: 
    #     await channel.send("<@"+str(id)+">님이 \""+message.content+"\"라고 말하였습니다.")
client.run(token)