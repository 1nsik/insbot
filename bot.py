import asyncio
import logging
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command


logging.basicConfig(level = logging.INFO)

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token = TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")

@dp.message(Command("reply"))
async def cmd_reply(message: types.Message):
    await message.reply("Hello00000!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

