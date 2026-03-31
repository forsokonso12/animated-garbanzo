import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv

# 1. Настройка логирования — крайне важно, чтобы видеть ошибки в панели Amvera
logging.basicConfig(level=logging.INFO)

# 2. Загрузка токена
load_dotenv()
# Amvera берет BOT_TOKEN из вкладки "Переменные"
BOT_TOKEN = os.getenv("BOT_TOKEN")

# 3. Инициализация
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# 4. Простой обработчик команды /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("✅ Бот успешно запущен и видит тебя!")

# 5. Эхо-режим: бот просто повторяет твой текст
@dp.message()
async def echo_handler(message: types.Message):
    await message.answer(f"Бот работает! Ты написал: {message.text}")

# 6. Точка входа (со всеми нужными подчеркиваниями)
async def main():
    logging.info("--- ПОПЫТКА ЗАПУСКА БОТА ---")
    await dp.start_polling(bot)

if name == "main":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Бот остановлен")