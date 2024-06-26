from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

class Survey(StatesGroup):
    name = State()
    age = State()
    sex = State()
    genre = State()
    film = State()
    actor = State()

survey_router = Router()

@survey_router.message(Command("survey"))
async def start_survey(message: types.Message, state: FSMContext):
    await state.set_state(Survey.name)
    await message.answer("Как вас зовут?")

@survey_router.message(Survey.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Survey.age)
    await message.answer("Сколько вам лет?")

@survey_router.message(Survey.age)
async def process_age(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(Survey.sex)
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Мужской", callback_data="male"),
                types.InlineKeyboardButton(text="Женский", callback_data="female")
            ]
        ]
    )
    await message.answer("Ваш пол?", reply_markup=kb)

@survey_router.callback_query(Survey.sex)
async def process_sex(callback_query: types.CallbackQuery, state: FSMContext):
    await state.update_data(sex=callback_query.data)
    await state.set_state(Survey.genre)
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(text="Боевик", callback_data="action")],
            [types.InlineKeyboardButton(text="Комедия", callback_data="comedy")],
            [types.InlineKeyboardButton(text="Драма", callback_data="drama")]
        ]
    )
    await callback_query.message.answer("Какой ваш любимый жанр фильмов?", reply_markup=kb)
    await callback_query.answer()

@survey_router.callback_query(Survey.genre)
async def process_genre(callback_query: types.CallbackQuery, state: FSMContext):
    await state.update_data(genre=callback_query.data)
    await state.set_state(Survey.film)
    await callback_query.message.answer("Какой ваш любимый фильм?")

@survey_router.message(Survey.film)
async def process_film(message: types.Message, state: FSMContext):
    await state.update_data(film=message.text)
    await state.set_state(Survey.actor)
    await message.answer("Какой ваш любимый актер?")

@survey_router.message(Survey.actor)
async def process_actor(message: types.Message, state: FSMContext):
    await state.update_data(actor=message.text)
    await state.clear()
    await message.answer("Спасибо за участие в опросе!")

