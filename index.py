import requests
import asyncio
import random
import urllib.request
import sqlite3
import aiohttp
import json
import webbrowser
import urllib.parse
import datetime
import logging
import threading
import os
import ctypes
from random import randint
from typing import List
from time import perf_counter
from pyrogram import Client, filters, sync
from pyrogram.errors import FloodWait
from io import StringIO
from config import *
from function import *
from time import sleep, perf_counter

stop = False
client = Client('session', '27447003', '112b12886c7fe281398799ef45d80d1f')
os.system('cls')
os.system('clear')
client.start()
client.stop()

print('\n' + BLUE + '[' + GREEN + 'INFO' + BLUE + ']' + WHITE + ' Bot aktivdir!\n' + BLUE + '[' + GREEN + 'INFO' + BLUE + ']' + WHITE + ' Dev: ' + GOLD + '@DucDeVulpe\n' + BLUE + '[' + GREEN + 'INFO' + BLUE + ']' + WHITE + ' Telegram kanal: ' + GOLD + 'https://t.me/CGGUB' + RESET)

@client.on_message(filters.command(spam_command, prefixes=commands_prefix) & filters.me)
def spam_message_handler(client, message):
    global stop
    args = message.text.split(' ')
    message.delete()
  
    if args[1] == 'stop':
        stop = True
        client.send_message(message.chat.id, 'Spam durduruldu!')
  
    else:
        i = int(args[1])
        message_text = ' '.join(args[2:])
        print(f'{BLUE}[{AQUA}LOG{BLUE}]{WHITE} Spam başladıldı! Mesaj sayı: {GOLD}{i}{WHITE}')
  
        try:
            for j in range(i):
                if stop:
                    stop = False
                    break
                client.send_message(message.chat.id, message_text)
                sleep(0.67)
        except FloodWait as e:
            sleep(e.x)   

@client.on_message(filters.command(ping_command, prefixes=commands_prefix) & filters.me)
def ping_message_handler(client, message):
    start = perf_counter()
    client.edit_message_text(message.chat.id, message.id, '<b>Pong!</b>')
    end = perf_counter()
    client.edit_message_text(message.chat.id, message.id, f'<b>Pong! {round(end - start, 3)} san.</b>')

@client.on_message(filters.command(help_command, prefixes=commands_prefix) & filters.me)
def help_message_handler(client, message):
    text = """
    **Prefikslər**: [.] - [/] - [!] - [-]
**Əmrlər**: https://telegra.ph/Komandy-04-28
👨‍💻 **Qurucu:** @DucTheVulpe
    """
    client.edit_message_text(message.chat.id, message.id, text, disable_web_page_preview=True)

@client.on_message(filters.command(love_command, prefixes=commands_prefix) & filters.me)
def love_message_handler(client, message):
    client.edit_message_text(message.chat.id, message.id, '🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
    client.edit_message_text(message.chat.id, message.id, '🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🧡🧡🤍🧡🧡🤍🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🤍🧡🧡🧡🧡🧡🤍🤍\n🤍🤍🤍🧡🧡🧡🤍🤍🤍\n🤍🤍🤍🤍🧡🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
    sleep(1/2)
    client.edit_message_text(message.chat.id, message.id, '🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💛💛🤍💛💛🤍🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍🤍💛💛💛💛💛🤍🤍\n🤍🤍🤍💛💛💛🤍🤍🤍\n🤍🤍🤍🤍💛🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
    sleep(1/2)
    client.edit_message_text(message.chat.id, message.id, '🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💚💚🤍💚💚🤍🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍🤍💚💚💚💚💚🤍🤍\n🤍🤍🤍💚💚💚🤍🤍🤍\n🤍🤍🤍🤍💚🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
    sleep(1/2)
    client.edit_message_text(message.chat.id, message.id, '🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💜💜🤍💜💜🤍🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍🤍💜💜💜💜💜🤍🤍\n🤍🤍🤍💜💜💜🤍🤍🤍\n🤍🤍🤍🤍💜🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
    sleep(1/2)
    client.edit_message_text(message.chat.id, message.id, '🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🖤🖤🤍🖤🖤🤍🤍\n🤍🖤🖤🖤🖤🖤🖤🖤🤍\n🤍🖤🖤🖤🖤🖤🖤🖤🤍\n🤍🖤🖤🖤🖤🖤🖤🖤🤍\n🤍🤍🖤🖤🖤🖤🖤🤍🤍\n🤍🤍🤍🖤🖤🖤🤍🤍🤍\n🤍🤍🤍🤍🖤🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
    sleep(1/2)
    client.edit_message_text(message.chat.id, message.id, '🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💖💖🤍💖💖🤍🤍\n🤍💖💖💖💖💖💖💖🤍\n🤍💖💖💖💖💖💖💖🤍\n🤍💖💖💖💖💖💖💖🤍\n🤍🤍💖💖💖💖💖🤍🤍\n🤍🤍🤍💖💖💖🤍🤍🤍\n🤍🤍🤍🤍💖🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
    sleep(1/2)
    client.edit_message_text(message.chat.id, message.id, '🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💌💌🤍💌💌🤍🤍\n🤍💌💌💌💌💌💌💌🤍\n🤍💌💌💌💌💌💌💌🤍\n🤍💌💌💌💌💌💌💌🤍\n🤍🤍💌💌💌💌💌🤍🤍\n🤍🤍🤍💌💌💌🤍🤍🤍\n🤍🤍🤍🤍💌🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
    client.edit_message_text(message.chat.id, message.id, '🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💙💙🤍💙💙🤍🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍🤍💙💙💙💙💙🤍🤍\n🤍🤍🤍💙💙💙🤍🤍🤍\n🤍🤍🤍🤍💙🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
    sleep(1/2)
    client.edit_message_text(message.chat.id, message.id, '❤️❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️❤️')
    sleep(1/2)
    client.edit_message_text(message.chat.id, message.id, '❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️')
    sleep(1/2)
    client.edit_message_text(message.chat.id, message.id, '❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️')
    sleep(1/2)
    client.edit_message_text(message.chat.id, message.id, '❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️')
    sleep(1/2)
    client.edit_message_text(message.chat.id, message.id, '❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️')
    sleep(1/2)
    client.edit_message_text(message.chat.id, message.id, '❤️❤️❤️❤️\n❤️❤️❤️❤️\n❤️❤️❤️❤️\n❤️❤️❤️❤️')
    sleep(1/2)
    client.edit_message_text(message.chat.id, message.id, '❤️❤️❤️\n❤️❤️❤️\n❤️❤️❤️')
    sleep(1/2)
    client.edit_message_text(message.chat.id, message.id, '❤️❤️\n❤️❤️')
    sleep(1/2)
    client.edit_message_text(message.chat.id, message.id, '❤️')


@client.on_message(filters.command(loves_command, prefixes=commands_prefix) & filters.me)
def loves_command_handler(client, message):
    time = 0.6
    for i in range(1):
        message.edit(f'''
✨✨✨✨✨✨
✨❤️❤️❤️❤️✨
✨❤️✨✨❤️✨
✨❤️❤️❤️❤️✨
✨✨✨❤️❤️✨
✨✨❤️✨❤️✨
✨❤️✨✨❤️✨
✨✨✨✨✨✨''')   
        sleep(time)
        message.edit(f'''
✨✨✨✨✨✨
✨❤️❤️❤️❤️✨
✨✨❤️❤️✨✨
✨✨❤️❤️✨✨
✨✨❤️❤️✨✨
✨✨❤️❤️✨✨
✨✨✨✨✨✨''')   
        sleep(time)
        message.edit(f'''
✨✨✨✨✨✨
✨❤️❤️❤️❤️✨
✨❤️✨✨✨✨
✨❤️❤️❤️✨✨
✨❤️✨✨✨✨
✨❤️❤️❤️❤️✨
✨✨✨✨✨✨''')
        sleep(time)
        message.edit(f'''
✨✨✨✨✨✨
✨❤️❤️❤️❤️✨
✨❤️✨✨✨✨
✨❤️❤️❤️❤️✨
✨❤️✨✨❤️✨
✨❤️✨✨❤️✨
✨❤️❤️❤️❤️✨
✨✨✨✨✨✨''')
        sleep(time)
        message.edit(f'''
✨✨✨✨✨✨
✨❤️❤️❤️❤️✨
✨❤️✨✨❤️✨
✨❤️❤️❤️❤️✨
✨✨✨❤️❤️✨
✨✨❤️✨❤️✨
✨❤️✨✨❤️✨
✨✨✨✨✨✨''')
        sleep(time)
        message.edit(f'''
✨✨✨✨✨✨✨✨✨
✨✨❤️❤️✨❤️❤️✨✨
✨❤️❤️❤️❤️❤️❤️❤️✨
✨❤️❤️❤️❤️❤️❤️❤️✨
✨✨❤️❤️❤️❤️❤️✨✨
✨✨✨❤️❤️❤️✨✨✨
✨✨✨✨❤️✨✨✨✨
✨✨✨✨✨✨✨✨✨''')
        sleep(time)
        message.edit(f'''
✨✨✨✨✨✨✨✨✨
✨✨💚💚✨💚💚✨✨
✨💚💚💚💚💚💚💚✨
✨💚💚💚💚💚💚💚✨
✨✨💚💚💚💚💚✨✨
✨✨✨💚💚💚✨✨✨
✨✨✨✨💚✨✨✨✨
✨✨✨✨✨✨✨✨✨''')
        sleep(time)
        message.edit(f'''
✨✨✨✨✨✨✨✨✨
✨✨💙💙✨💙💙✨✨
✨💙💙💙💙💙💙💙✨
✨💙💙💙💙💙💙💙✨
✨✨💙💙💙💙💙✨✨
✨✨✨💙💙💙✨✨✨
✨✨✨✨💙✨✨✨✨
✨✨✨✨✨✨✨✨✨''')
        sleep(time)
        message.edit(f'''
✨✨✨✨✨✨✨✨✨
✨✨💜💜✨💜💜✨✨
✨💜💜💜💜💜💜💜✨
✨💜💜💜💜💜💜💜✨
✨✨💜💜💜💜💜✨✨
✨✨✨💜💜💜✨✨✨
✨✨✨✨💜✨✨✨✨
✨✨✨✨✨✨✨✨✨''')
        sleep(time)
        message.edit(f'''
✨✨✨✨✨✨✨✨✨
✨✨🤍🤍✨🤍🤍✨✨
✨🤍🤍🤍🤍🤍🤍🤍✨
✨🤍🤍🤍🤍🤍🤍🤍✨
✨✨🤍🤍🤍🤍🤍✨✨
✨✨✨🤍🤍🤍✨✨✨
✨✨✨✨🤍✨✨✨✨
✨✨✨✨✨✨✨✨✨''')
        sleep(time)
        message.edit(f'''
✨✨✨✨✨✨✨✨✨
✨✨🖤🖤✨🖤🖤✨✨
✨🖤🖤🖤🖤🖤🖤🖤✨
✨🖤🖤🖤🖤🖤🖤🖤✨
✨✨🖤🖤🖤🖤🖤✨✨
✨✨✨🖤🖤🖤✨✨✨
✨✨✨✨🖤✨✨✨✨
✨✨✨✨✨✨✨✨✨''')
        sleep(time)
        message.edit(f'''
✨✨✨✨✨✨✨✨✨
✨✨💛💛✨💛💛✨✨
✨💛💛💛💛💛💛💛✨
✨💛💛💛💛💛💛💛✨
✨✨💛💛💛💛💛✨✨
✨✨✨💛💛💛✨✨✨
✨✨✨✨💛✨✨✨✨
✨✨✨✨✨✨✨✨✨''')
        sleep(time)
        message.edit(f'''
✨✨✨✨✨✨✨✨✨
✨✨🧡🧡✨🧡🧡✨✨
✨🧡🧡🧡🧡🧡🧡🧡✨
✨🧡🧡🧡🧡🧡🧡🧡✨
✨✨🧡🧡🧡🧡🧡✨✨
✨✨✨🧡🧡🧡✨✨✨
✨✨✨✨🧡✨✨✨✨
✨✨✨✨✨✨✨✨✨''')
        sleep(3)

@client.on_message(filters.command(like_command, prefixes=commands_prefix) & filters.me)
def like_command_handler(client, message):
    time = 0.6
    for i in range(1):
        message.edit(f'''      
🟦''')   
        sleep(0.001)
        message.edit(f'''
🟦🟦''')   
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦️''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦️''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦🟦''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦🟦🟦''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦🟦🟦🟦''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦🟦🟦🟦🟦''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦🟦🟦🟦🟦🟦''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦🟦🟦🟦🟦🟦🟦''')
        sleep(5)

@client.on_message(filters.command(dislike_command, prefixes=commands_prefix) & filters.me)
def dislike_command_handler(client, message):
    time = 0.6
    for i in range(1):
        message.edit(f'''
🟥''')   
        sleep(0.001)
        message.edit(f'''
🟥🟥''')   
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥️''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️🟥''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥🟥''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥🟥🟥''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥🟥🟥🟥''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥''')
        sleep(1)
        message.edit(f'''
🈲🈲🈲🈲🈲🈲🈲🈲
🈲🈲⬜️⬜️⬜️🈲⬜️🈲
🈲🈲⬜️⬜️⬜️🈲⬜️🈲
🈲⬜️⬜️⬜️⬜️🈲⬜️🈲
🈲🈲🈲🈲⬜️🈲🈲🈲
🈲🈲🈲🈲🈲🈲🈲🈲''')
        sleep(1)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥
''')
        sleep(1)
        message.edit(f'''
🈲🈲🈲🈲🈲🈲🈲🈲
🈲🈲⬜️⬜️⬜️🈲⬜️🈲
🈲🈲⬜️⬜️⬜️🈲⬜️🈲
🈲⬜️⬜️⬜️⬜️🈲⬜️🈲
🈲🈲🈲🈲⬜️🈲🈲🈲
🈲🈲🈲🈲🈲🈲🈲🈲''')
        sleep(4)

@client.on_message(filters.command(profile_command, prefixes=commands_prefix) & filters.me)
def profile_command_handler(client, message):
    global start_date, message_count
    cursor.execute('SELECT start_date FROM relationship')
    result = cursor.fetchone()
    if result:
        start_date = datetime.datetime.strptime(result[0], "%d.%m.%Y")
    else:
        start_date = None
    
    if start_date is None:
        text = f"""💾 <b>Profil:</b>

<b>User:</b> <code>{message.from_user.first_name}</code>
<b>Chat ID:</b> <code>{message.chat.id}</code>
<b>User ID:</b> <code>{message.from_user.id}</code>
"""
@client.on_message(filters.command(type_command, prefixes=commands_prefix) & filters.me)
def type_command_handler(client, message):
    orig_text = message.text.split("type ", maxsplit=1)[1]
    text = orig_text
    tbp = ""
    typing_symbol = "█"
    while (tbp != orig_text):
        try:
            message.edit(tbp + typing_symbol)
            sleep(0.05)

            tbp = tbp + text[0]
            text = text[1:]

            message.edit(tbp)
            sleep(0.05)

        except FloodWait as e:
            sleep(e.x)

@client.on_message(filters.command(timer_command, prefixes=commands_prefix) & filters.me)
async def timer_command_handler(client, message):
    if len(message.command) == 1:
        await message.edit("Не указано время.")
        return
    try:
        time = int(message.command[1])
    except ValueError:
        await message.edit("Yanlış arqument.")
        return
    for i in range(time, -1, -1):
        minutes, seconds = divmod(i, 60)
        time_str = f"{minutes:02d}:{seconds:02d} ⏰"
        await message.edit(time_str)
        await asyncio.sleep(1)
    await message.edit("Vaxt bitti! ⏰⏰⏰")

@client.on_message(filters.command(write_command, prefixes=commands_prefix) & filters.me)
async def write_command_handler(client, message):
    if len(message.command) < 2:
        return await message.reply_text("Mətni yazın")
    m = await message.reply_text("Yazılır...")
    name = (
        message.text.split(None, 1)[1]
        if len(message.command) < 3
        else message.text.split(None, 1)[1].replace(" ", "%20")
    )
    hand = "https://apis.xditya.me/write?text=" + name
    await m.edit("Yüklənir...")
    await m.delete()
    await message.reply_photo(hand)

@client.on_message(filters.text & ~filters.me)
def message_handler(client, message):
    global message_count, start_date
    if start_date is not None:
        message_count += 1

start_date = None
message_count = 0

conn = sqlite3.connect('bot_data.db', check_same_thread=False)
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS relationship
                  (id integer primary key, start_date text)''')
conn.commit()

conn = sqlite3.connect('bot_data.db', check_same_thread=False)
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS relationship
                  (id integer primary key, start_date text)''')
conn.commit()

@client.on_message(filters.command(information_command, prefixes=commands_prefix) & filters.me)
async def information_message_handler(client, message):
    username = message.text.split(f'{message.command[0]} ')[-1]
    user = await client.get_users(username)
    if user:
        first_name = user.first_name if user.first_name else '❌'
        last_name = user.last_name if user.last_name else '❌'
        mention = user.mention if user.mention else '❌'
        is_scam = '✅' if hasattr(user, 'is_scam') and user.is_scam else '❌'
        is_premium = '✅' if hasattr(user, 'is_premium') and user.is_premium else '❌'
        language_code = user.language_code if hasattr(user, 'language_code') else '❌'
        emoji_status = user.emoji_status if hasattr(user, 'emoji_status') else '❌'
        phone_number = user.phone_number if hasattr(user, 'phone_number') else '❌'
        text = f'👤 Имя: {first_name}\n👥 Фамилия: {last_name}\n📌 Упоминание: {mention}\n❗️ Scam: {is_scam}\n💎 Telegram Premium: {is_premium}\n🌐 Язык: {language_code}\n😀 Эмодзи статус: {emoji_status}\n☎️ Телефон: {phone_number}'
        await client.send_message(message.chat.id, text)
    else:
        await client.send_message(message.chat.id, f'Пользователь {username} не найден')

@client.on_message(filters.command(message_command, prefixes=commands_prefix) & filters.me)
async def message_message_handler(client, message):
    args = message.text.split(maxsplit=2)[1:]
    delay = args[0].split()
    text = args[1]
    delay_seconds = 0
    
    for d in delay:
        if d.endswith("ч"):
            delay_seconds += int(d[:-1]) * 3600
        elif d.endswith("м"):
            delay_seconds += int(d[:-1]) * 60
        elif d.endswith("с"):
            delay_seconds += int(d[:-1])
    
    await asyncio.sleep(delay_seconds)
    await client.send_message(message.chat.id, text)

@client.on_message(filters.command(hug_command, prefixes=commands_prefix) & filters.me)
async def hug_message_handler(client, message):
    reply_msg = message.reply_to_message
    if not reply_msg:
        await message.edit_text("Необходимо ответить на сообщение пользователя, которого нужно обнять.")
        return
    user = reply_msg.from_user
    first_name = message.from_user.first_name
    random_gif = f"gifs/hug/{random.randint(1, 10)}.gif"
    try:
        await client.send_animation(
            chat_id=message.chat.id,
            animation=random_gif,
            reply_to_message_id=message.id,
        )
    except Exception as e:
        logging.exception(e)
        await message.edit_text("Не удалось отправить gif.")
        return
    await message.edit_text(f"{first_name} обнял(а) {user.mention}.")

@client.on_message(filters.command(kiss_command, prefixes=commands_prefix) & filters.me)
async def kiss_message_handler(client, message):
    reply_msg = message.reply_to_message
    if not reply_msg:
        await message.edit_text("Необходимо ответить на сообщение пользователя, которого нужно поцеловать.")
        return
    user = reply_msg.from_user
    first_name = message.from_user.first_name
    random_gif = f"gifs/kiss/{random.randint(1, 10)}.gif"
    try:
        await client.send_animation(
            chat_id=message.chat.id,
            animation=random_gif,
            reply_to_message_id=message.id,
        )
    except Exception as e:
        logging.exception(e)
        await message.edit_text("Не удалось отправить gif.")
        return
    await message.edit_text(f"{first_name} поцеловал(а) {user.mention}.")

@client.on_message(filters.command(hit_command, prefixes=commands_prefix) & filters.me)
async def hit_message_handler(client, message):
    reply_msg = message.reply_to_message
    if not reply_msg:
        await message.edit_text("Необходимо ответить на сообщение пользователя, которого нужно ударить.")
        return
    user = reply_msg.from_user
    first_name = message.from_user.first_name
    random_gif = f"gifs/hit/{random.randint(1, 10)}.gif"
    try:
        await client.send_animation(
            chat_id=message.chat.id,
            animation=random_gif,
            reply_to_message_id=message.id,
        )
    except Exception as e:
        logging.exception(e)
        await message.edit_text("Не удалось отправить gif.")
        return
    await message.edit_text(f"{first_name} ударил(а) {user.mention}.")

@client.on_message(filters.command(bite_command, prefixes=commands_prefix) & filters.me)
async def bite_message_handler(client, message):
    reply_msg = message.reply_to_message
    if not reply_msg:
        await message.edit_text("Необходимо ответить на сообщение пользователя, которого нужно укусить.")
        return
    user = reply_msg.from_user
    first_name = message.from_user.first_name
    random_gif = f"gifs/bite/{random.randint(1, 10)}.gif"
    try:
        await client.send_animation(
            chat_id=message.chat.id,
            animation=random_gif,
            reply_to_message_id=message.id,
        )
    except Exception as e:
        logging.exception(e)
        await message.edit_text("Не удалось отправить gif.")
        return
    await message.edit_text(f"{first_name} укусил(а) {user.mention}.")

@client.on_message(filters.command(dice_command, prefixes=commands_prefix) & filters.me)
async def dice_command_handler(client, message):
    
    number = randint(1, 6)
    
    await message.edit(f"🎲 {number}")

@client.on_message(filters.command(loved_command, prefixes=commands_prefix) & filters.me)
async def loved_message_handler(client, message):
    animation = [
        '❤️', '🧡❤️', '💛🧡❤️', '💚💛🧡❤️', '💙💚💛🧡❤️', '💜💙💚💛🧡❤️', '🤍💜💙💚💛🧡❤️', 
        '❤️🤍💜💙💚💛🧡', '🧡❤️🤍💜💙💚💛', '💛🧡❤️🤍💜💙💚', '💚💛🧡❤️🤍💜💙', '💙💚💛🧡❤️🤍💜', 
        '💜💙💚💛🧡❤️🤍', '🤍💜💙💚💛🧡❤️', '❤️🤍💜💙💚💛', '🧡❤️🤍💜💙💚', '💛🧡❤️🤍💜💙',
        '💚💛🧡❤️🤍💜', '💙💚💛🧡❤️🤍', '💜💙💚💛🧡❤️', '🤍💜💙💚💛', '❤️🤍💜💙💚', 
        '🧡❤️🤍💜💙', '💛🧡❤️🤍💜', '💚💛🧡❤️🤍', '💙💚💛🧡❤️', '💜💙💚💛🧡', '❤️🤍💜💙💚', 
        '🧡❤️🤍💜💙', '💛🧡❤️🤍💜', '💚💛🧡❤️🤍', '💙💚💛🧡', '💜💙💚💛', '🤍💜💙💚', '❤️🤍💜💙', 
        '🧡❤️🤍💜', '💛🧡❤️🤍', '💚💛🧡', '💙💚', '💜'
    ]
    
    for i in range(2):
        for heart in animation:
            await asyncio.sleep(0.5)
            await message.edit(heart)


@client.on_message(filters.command(crypto_command, prefixes=commands_prefix) & filters.me)
async def crypto_message_handler(client, message):
    crypto_info = crypto()
    await message.reply(crypto_info)

client.run()
