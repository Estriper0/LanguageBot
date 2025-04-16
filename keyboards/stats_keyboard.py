from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def get_stats_keyboard():
    btn = InlineKeyboardButton(text='Назад', callback_data='back')
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[btn]])
    return keyboard