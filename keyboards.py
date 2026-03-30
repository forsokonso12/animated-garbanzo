
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

def main_kb():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📊 Баланс"), KeyboardButton(text="🏠 Обязательные траты")],
            [KeyboardButton(text="📉 Долги и Вклады"), KeyboardButton(text="⚙️ Настройки")]
        ],
        resize_keyboard=True
    )

def balance_inline_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💰 ЗП Пришла!"), callback_data="salary_arrived"],
        [InlineKeyboardButton(text="📋 История"), callback_data="history"]
    ])
EOF