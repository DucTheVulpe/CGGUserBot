from config import PREFIX
import asyncio
import time
from datetime import datetime
from pyrogram import filters
from CGG import app, StartTime, CMD_HELP
from sys import version_info

from pyrogram import __version__ as __pyro_version__
from pyrogram.types import Message

CMD_HELP.update(
    {
        "Alive": """
『 **Alive** 』
  `alive` -> Bu əmr botun çalışdığını göstərir.
  `ping` -> Sizə botun cavab sürətini göstərir.
"""
    }
)

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["san", "dəq", "saat", "gün"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += " ".join(time_list)

    return ping_time


@app.on_message(filters.command("alive", PREFIX) & filters.me)
async def alive(_, m):
    start_time = time.time()
    uptime = get_readable_time((time.time() - StartTime))
    reply_msg = f"**[CGGUserBot](https://t.me/CGGUserBot)**\n"
    reply_msg += f"__Python__: `{__python_version__}`\n"
    reply_msg += f"__@Pyrogram__: `{__pyro_version__}`\n"
    end_time = time.time()
    reply_msg += f"__CGG aktivdir__: {uptime}\n"
    reply_msg += f"__Qurucu__: @DucDeVulpe"
    photo = "https://telegra.ph/file/2c43a3f5381e507da915d.jpg"
    await m.delete()
    if m.reply_to_message:
        await app.send_photo(
            m.chat.id,
            photo,
            caption=reply_msg,
            reply_to_message_id=m.reply_to_message.id,
        )
    else:
        await app.send_photo(m.chat.id, photo, caption=reply_msg)


@app.on_message(filters.command("ping", PREFIX) & filters.me)
async def pingme(_, message: Message):
    start = datetime.now()
    await message.edit("`Pong!`")
    end = datetime.now()
    m_s = (end - start).microseconds / 1000
    await message.edit(f"**Pong!**\n`{m_s} ms`")
