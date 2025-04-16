from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def get_study_keyboard():
    btn_1 = InlineKeyboardButton(text='Погода', callback_data='weather')
    btn_2 = InlineKeyboardButton(text='Семья', callback_data='family')
    btn_3 = InlineKeyboardButton(text='Еда', callback_data='food')
    btn_4 = InlineKeyboardButton(text='Назад', callback_data='back')
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[btn_1], [btn_2], [btn_3], [btn_4]])
    return keyboard