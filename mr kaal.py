import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

TOKEN = "7278506363:AAHOn56nJ7k-gMRNYlbqqlQ47soSK8wD3pM"

bot = Bot(token=TOKEN)
dp = Dispatcher()  # ✅ Correct way in Aiogram v3

@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Hello! This is your AI-powered bot.")

async def main():
    await dp.start_polling(bot)  # ✅ Bas dispatcher chalu kar

if __name__ == "__main__":
    asyncio.run(main())
