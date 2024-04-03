from pyrogram import idle, Client, filters
from config import PREFIX
from cgg import app
import logging
from cgg.modules import *

app.start()
me = app.get_me()
print(f"CGG UserBot started for user {me.id}. Type {PREFIX}help in any telegram chat.")
idle()