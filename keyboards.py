from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Главное меню
main_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        # Вот здесь скобка закрывается строго В КОНЦЕ строки
        InlineKeyboardButton(text="💰 ЗП Пришла!", callback_data="salary_arrived")
    ],
    [
        InlineKeyboardButton(text="📉 Добавить расход", callback_data="add_expense"),
        InlineKeyboardButton(text="📈 Добавить доход", callback_data="add_income")
    ],
    [
        InlineKeyboardButton(text="📊 Статистика", callback_data="show_stats"),
        InlineKeyboardButton(text="⚙️ Настройки", callback_data="settings")
    ]
])

# Клавиатура отмены (если нужно прервать ввод данных)
cancel_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="❌ Отмена", callback_data="cancel")]
])

# Клавиатура подтверждения
confirm_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="✅ Подтвердить", callback_data="confirm"),
        InlineKeyboardButton(text="🔄 Изменить", callback_data="edit")
    ]
])