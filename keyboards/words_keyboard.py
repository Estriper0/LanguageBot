from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


async def get_words_keyboard(words, right):
    kb_builder = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = []
    for i in range(len(words)):
        if i == right:
            buttons.append(InlineKeyboardButton(text=words[i].word_rus, callback_data='right'))
        else:
            buttons.append(InlineKeyboardButton(text=words[i].word_rus, callback_data='wrong'))
    kb_builder.row(*buttons, width=2)
    kb_builder.row(InlineKeyboardButton(text='Остановиться', callback_data='stop_study'))
    return kb_builder.as_markup()


async def get_continue_keyboard():
    btn_1 = InlineKeyboardButton(text='Продолжить', callback_data='continue')
    btn_2 = InlineKeyboardButton(text='Остановиться', callback_data='stop_study')
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[btn_1], [btn_2]])
    return keyboard