import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, types, F
from handlers.common import rt as common_router
from dotenv import load_dotenv


load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    exit("Токен бота не найден.")

bot = Bot(token = BOT_TOKEN)
dp = Dispatcher()

async def main():
    logging.basicConfig(level=logging.INFO)

    dp.include_router(common_router)

    await bot.delete_webhook(drop_pending_updates=True)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
