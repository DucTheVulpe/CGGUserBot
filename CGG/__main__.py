from pyrogram import idle, Client, filters
from config import PREFIX
from CGG import app
import logging
from CGG.modules import *

app.start()
me = app.get_me()
print(f"CGGUserBot {me.id} üçün başladılmışdır. İstədiyiniz çatda {PREFIX}alive yazın.")
idle()
