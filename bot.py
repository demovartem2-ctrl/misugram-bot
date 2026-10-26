import asyncio, logging, os, random
from aiogram import Bot, Dispatcher, F
from aiogram.client.telegram import TelegramAPIServer
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.types import Message

logging.basicConfig(level=logging.INFO)

TOKEN = "1780243260:JsuCWrdBDfMjPxmH2JRVNZ9hREvWYzDZ0fe"
API_BASE = "https://misugram.cloud-ip.cc"

REPLIES = ["иди нахуй", "пошёл нахуй", "нахуй иди", "да пошёл ты"]

session = AiohttpSession(api=TelegramAPIServer.from_base(API_BASE))
bot = Bot(token=TOKEN, session=session)
dp = Dispatcher()

@dp.message(F.text)
async def reply(message: Message):
    if message.text.startswith("/"):
        return
    await message.reply(random.choice(REPLIES))

async def main():
    me = await bot.get_me()
    logging.info("Bot started as @%s", me.username)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
