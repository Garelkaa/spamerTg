from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import time
from time import sleep
from pyrogram.types import Message

botId = ... #BotId
botId2 = ... #BotId

api_id = 123 #apiId
api_hash = "" #apwhashKey

app = Client("my_account", api_id=api_id, api_hash=api_hash)
# app2 = Client("my_accounssd")

@app.on_message(filters.command("activate", prefixes=".") & filters.me)
def type(_, msg):
    timer = 14400  #
    while True:
        app.send_message(botId, text)
        sleep(.1)
        app.send_message(botId2, text)
        sleep(.1)
        app.send_message(botId, text)
        sleep(.1)
        app.send_message(botId2, text)
        sleep(1)
    

app.run()
