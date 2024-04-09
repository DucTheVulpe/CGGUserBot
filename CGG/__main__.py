from pyrogram import idle, Client, filters
from config import PREFIX
from CGG import app
import logging
from CGG.modules import *

app.start()
me = app.get_me()
print(f"CGGUserBot started for user {me.id}. Type {PREFIX}help in any telegram chat.")
idle()
