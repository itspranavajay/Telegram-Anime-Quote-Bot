import requests
import rapidjson as json
from PIL import Image
import os
import asyncio
import re
from config import bot_token
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


anime = Client(
    ":memory:",
    bot_token="1688991183:AAE5Y2HIroqZKRRggWci4ofkdevdEnMf4ec",
    api_id=2114829,
    api_hash="e90ddf1f46ac58ee0c267eff1e0548de",
)



messageprivate = '''
Hi, I'm Anime Quotes Bot
'''

messagegroup = '''
Hi, I'm Anime Quotes bot
'''





@anime.on_message(filters.command(["start"], prefixes=["/", "!"]))
async def start(_, message):
    self = await anime.get_me()
    busername = self.username
    if message.chat.type != "private":
        await message.reply_text(messagegroup)
        return
    else:
        buttons = [[InlineKeyboardButton("Github", url="https://github.com/MoeZilla/Telegram-Anime-Quotes-Bot"),
                    ]]
        await message.reply_text(messageprivate, reply_markup=InlineKeyboardMarkup(buttons))


@anime.on_message(filters.command("quote"))
def quote(_, message):
    quote = requests.get("https://animechan.vercel.app/api/random").json()
    message.reply_text('`'❝+quote['quote']+'`\n '+quote['anime']+' In '+quote['character']+')

print(
    """
Please Follow MoeZilla 👀✨
""" 
)


anime.run()

