import logging
from aiogram import types, Router, F
from aiogram.filters import Command

start_router = Router()

@start_router.message(Command("start"))
async def start(message: types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Расписание сеансов", url="https://examplecinema.com")
            ],
            [
                types.InlineKeyboardButton(text="Наш Instagram", url="https://instagram.com/examplecinema")
            ],
            [
                types.InlineKeyboardButton(text="Наш Twitter", url="https://twitter.com/examplecinema")
            ],
            [
                types.InlineKeyboardButton(text="О кинотеатре", callback_data="about_cinema")
            ],
            [
                types.InlineKeyboardButton(text="Бронировать билеты", callback_data="book_tickets")
            ],
            [
                types.InlineKeyboardButton(text="Боевик", callback_data="genre_action")
            ],
            [
                types.InlineKeyboardButton(text="Комедия", callback_data="genre_comedy")
            ],
            [
                types.InlineKeyboardButton(text="Драма", callback_data="genre_drama")
            ]
        ]
    )
    logging.info(message.from_user)
    await message.answer(f"Привет, {message.from_user.first_name}! Добро пожаловать в наш кинобот.", reply_markup=kb)

@start_router.callback_query(F.data == "about_cinema")
async def about_cinema(callback: types.CallbackQuery):
    await callback.message.answer("Информация о кинотеатре")

@start_router.callback_query(F.data == "book_tickets")
async def book_tickets(callback: types.CallbackQuery):
    await callback.message.answer("Выберите фильм и сеанс для бронирования билетов")

