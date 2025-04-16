from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def get_menu_keyboard():
    btn_1 = InlineKeyboardButton(text='Изучать', callback_data='start_study')
    btn_2 = InlineKeyboardButton(text='Статистика', callback_data='stats')
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[btn_1], [btn_2]])
    return keyboard