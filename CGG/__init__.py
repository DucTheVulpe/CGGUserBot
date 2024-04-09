import logging
import sys
import time
from pyrogram import Client, errors
from config import API_HASH, API_ID
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [CGG] - %(levelname)s - %(message)s",
)

logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("apscheduler").setLevel(logging.ERROR)

HELP = {}
CMD_HELP = {}

StartTime = time.time()

API_ID = API_ID
API_HASH = API_HASH

app = Client("cgg", api_id=API_ID, api_hash=API_HASH)
