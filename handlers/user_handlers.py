from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command, StateFilter
from aiogram.fsm.state import default_state

from keyboards.menu_keyboard import get_menu_keyboard
from keyboards.study_keyboard import get_study_keyboard
from keyboards.stats_keyboard import get_stats_keyboard
from database.methods import register_user, select_user


router = Router()


@router.message(CommandStart(), StateFilter(default_state))
async def start_bot(message: Message):
    keyboard = await get_menu_keyboard()
    await register_user(message.from_user.id)
    await message.answer('👋Привет! Это бот для изучения иностранных языков\nРад тебя видеть)✨', reply_markup=keyboard)


@router.message(Command(commands='help'), StateFilter(default_state))
async def help(message: Message):
    keyboard = await get_menu_keyboard()
    await message.answer('✨Чем бы вы хотели заняться?', reply_markup=keyboard)


@router.callback_query(F.data == 'start_study', StateFilter(default_state))
async def start_study(callback: CallbackQuery):
    keyboard = await get_study_keyboard()
    await callback.message.delete()
    await callback.message.answer(text='📚 Что вы хотите узнать сегодня? Выберите категорию!', reply_markup=keyboard)


@router.callback_query(F.data == 'stats', StateFilter(default_state))
async def stats(callback: CallbackQuery):
    keyboard = await get_stats_keyboard()
    user = await select_user(callback.from_user.id)
    await callback.message.delete()
    await callback.message.answer(text=f'🏆 Вот как у вас идут дела на данный момент:\n💡 Верно отгаданных слов - <b>{user.score}</b>', reply_markup=keyboard)


@router.callback_query(F.data == 'back', StateFilter(default_state))
async def back(callback: CallbackQuery):
    keyboard = await get_menu_keyboard()
    await callback.message.delete()
    await callback.message.answer('✨Чем бы вы хотели заняться?', reply_markup=keyboard)


@router.message(StateFilter(default_state))
async def other_menu(message: Message):
    keyboard = await get_menu_keyboard()
    await message.answer('❌ Упс! Я не понял. \n💡 Попробуйте один из этих вариантов:', reply_markup=keyboard)
