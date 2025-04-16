import random
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from database.methods import choose_category, new_score
from keyboards.words_keyboard import get_words_keyboard, get_continue_keyboard
from keyboards.menu_keyboard import get_menu_keyboard


router = Router()


class FSMStudy(StatesGroup):
    study = State()


@router.callback_query(F.data.in_(['weather', 'family', 'food', 'continue']))
async def choose_words(callback: CallbackQuery, state: FSMContext):
    if callback.data == 'continue':
        data = await state.get_data()
        words = random.sample(await choose_category(data['cat']), 4)
    else:
        await state.update_data(cat=callback.data)
        words = random.sample(await choose_category(callback.data), 4)
    num_word = random.randrange(4)
    keyboard = await get_words_keyboard(words, num_word)
    await state.update_data(word_rus=words[num_word].word_rus, word_eng=words[num_word].word_eng)
    await callback.message.delete()
    await callback.message.answer(f'🤔 Какой будет перевод: <b>{words[num_word].word_eng}</b>', reply_markup=keyboard)
    await state.set_state(FSMStudy.study)


@router.callback_query(F.data == 'wrong', StateFilter(FSMStudy.study))
async def wrong_answer(callback: CallbackQuery, state: FSMContext):
    keyboard = await get_continue_keyboard()
    data = await state.get_data()
    await callback.message.delete()
    await callback.message.answer(f'😅 Упс! Не волнуйтесь! Ошибки — это часть обучения. 🌟\nПравильный перевод: <b><u>{data['word_eng']} - {data['word_rus']}</u></b> \nХочешь продолжить? 💭', reply_markup=keyboard)


@router.callback_query(F.data == 'right', StateFilter(FSMStudy.study))
async def right_answer(callback: CallbackQuery, state: FSMContext):
    keyboard = await get_continue_keyboard()
    data = await state.get_data()
    if "score" in data:
        await state.update_data(score=(data['score'] + 1))
    else:
        await state.update_data(score=1)
    await callback.message.delete()
    await callback.message.answer('🎉 Отличная работа! Ты супер! 💪 Так держать! 🚀 \nХочешь продолжить? 💭', reply_markup=keyboard)


@router.callback_query(F.data == 'stop_study', StateFilter(FSMStudy.study))
async def stop_study(callback: CallbackQuery, state: FSMContext):
    keyboard = await get_menu_keyboard()
    data = await state.get_data()
    if 'score' in data:
        await new_score(callback.from_user.id, data['score'])
    await state.clear()
    await callback.message.delete()
    await callback.message.answer('👋 Закончили на сегодня? \n✨ Возвращайтесь скорее, чтобы продолжить улучшать свой английский!', reply_markup=keyboard)


@router.message(StateFilter(FSMStudy.study))
async def other_study(message: Message):
    keyboard = await get_continue_keyboard()
    await message.answer('Ты хочешь закончить?😢', reply_markup=keyboard)


