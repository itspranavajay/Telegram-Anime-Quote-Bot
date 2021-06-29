import requests
import rapidjson as json
from PIL import Image
import os
import asyncio
import re
from config import bot_token
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


anime = Client(
    ":memory:",
    bot_token="token",
    api_id=266226,
    api_hash="api hash",
)



messageprivate = '''
Hi, I'm Anime Quotes Bot
'''

messagegroup = '''
Hi, I'm Anime Quotes bot
'''





@anime.on_message(filters.command(["start"], prefixes=["/", "!"]))
async def start(_, message):
    self = await eliana.get_me()
    busername = self.username
    if message.chat.type != "private":
        await message.reply_text(messagegroup)
        return
    else:
        buttons = [[InlineKeyboardButton("Github", url="https://github.com/MoeZilla/Telegram-Anime-Quotes-Bot"),
                    ]]
        await message.reply_text(messageprivate, reply_markup=InlineKeyboardMarkup(buttons))


@anime.on_message(filters.command("quote"))
def truth(_, message):
    quote = requests.get("https://animechan.vercel.app/api/random").json()
    quote = quote.get("quote")
    message.reply_text(quote)

print(
    """
Please Follow MoeZilla 👀✨
"""
)


eliana.run()

