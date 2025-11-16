import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

TOKEN = os.getenv("BOT_TOKEN")
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("سلام میلاد! ربات کریپتو فعال شد ✅")

@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.reply("دستورات:\n/start - شروع\n/help - راهنما")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)# crypto-bot
ربات تلگرام برای پیش‌بینی ارز دیجیتال
