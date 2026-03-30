
import asyncio
import os
import logging
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage

import database as db
import keyboards as kb

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Загрузка переменных
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

# --- Обработка команды /start ---
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    db.create_user(message.from_user.id)
    await message.answer(
        "👋 Привет! Я твой новый финансовый бот.\n\n"
        "Я буду удалять твои сообщения с цифрами, чтобы чат был чистым.", 
        reply_markup=kb.main_kb()
    )

# --- Кнопка "Баланс" ---
@dp.message(F.text == "📊 Баланс")
async def show_balance(message: types.Message):
    await message.delete()  # Удаляем само нажатие кнопки
    user = db.get_user(message.from_user.id)
    balance = user['balance'] if user else 0
    
    text = f"📊 Ваш баланс: {balance:,.2f} руб.\n\n" \
           f"Просто пришли мне число (например, 500), чтобы записать расход."
    await message.answer(text, reply_markup=kb.balance_inline_kb(), parse_mode="Markdown")

# --- Логика записи расхода (удаляет сообщение пользователя) ---
@dp.message(lambda message: message.text and message.text.replace('.', '', 1).isdigit())
async def process_expense(message: types.Message):
    amount = float(message.text.replace(',', '.'))
    uid = message.from_user.id
    
    # Записываем в базу данных
    db.add_transaction(uid, amount, "expense")
    
    # 1. Удаляем сообщение пользователя с цифрой (для чистоты)
    await message.delete()
    
    # 2. Отправляем временное подтверждение
    temp_msg = await message.answer(f"✅ Записан расход: {amount} руб.")
    
    # 3. Через 3 секунды удаляем подтверждение, чтобы не мусорить
    await asyncio.sleep(3)
    await temp_msg.delete()

# --- Запуск бота ---
async def main():
    db.init_db()  # Создаем таблицы при старте
    print("🚀 Бот успешно запущен на сервере!")
    await dp.start_polling(bot)

if name == "main":
    asyncio.run(main())
EOF