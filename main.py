import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv

# Загружаем переменные (для локальной работы)
load_dotenv()

# Берем токен из переменных окружения
# В Amvera мы его уже добавили в разделе "Переменные"
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Обработчик команды /start
@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("Привет! Я живой и работаю на Amvera! Отправь мне что-нибудь.")

# Обработчик любого текста (Эхо)
@dp.message()
async def echo_handler(message: types.Message):
    await message.answer(f"Ты написал: {message.text}")

async def main():
    print("Бот запущен и готов к работе...")
    await dp.start_polling(bot)

if name == "main":
    asyncio.run(main())