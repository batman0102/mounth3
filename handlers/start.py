import logging
from aiogram import types, Router, F
from aiogram.filters import Command
from bot import *
from crawler.cinema import *

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
                types.InlineKeyboardButton(text="Космос", callback_data="space_action")
            ],
            [
                types.InlineKeyboardButton(text="Фентези", callback_data="genre_fant")
            ],
            [
                types.InlineKeyboardButton(text="Комедия", callback_data="genre_comedy")
            ],
            [
                types.InlineKeyboardButton(text="Аниме", callback_data="anime")
            ]
        ]
    )
    logging.info(message.from_user)
    await message.answer(f"Привет, {message.from_user.first_name}! Добро пожаловать в наш кинобот «Broadway».", reply_markup=kb)

@start_router.callback_query(F.data == "about_cinema")
async def about_cinema(callback: types.CallbackQuery):
    await callback.message.answer("КИНОТЕАТР «Broadway» - один из самых больших кинокомплексов Кыргызстана! Новый, современный кинотеатр, 7 кинозалами, рассчитанный на 805 мест, также вы можете насладиться первым VIP залом отличающимся своей комфортабельностью. ")

@start_router.callback_query(F.data == "book_tickets")
async def book_tickets(callback: types.CallbackQuery):
    await callback.message.answer("Выберите фильм и сеанс для бронирования билетов")

@start_router.callback_query(F.data == "space_action")
async def space_movies(callback: types.CallbackQuery):
    movies = db.get_movies_by_category(1)
    if movies:
        response = '\n'.join([f"{movie[1]} - {movie[2]} - {movie[3]} - {movie[4]}" for movie in movies])
    else:
        response = "Список фильмов пуст."
    await callback.message.answer(response)

@start_router.callback_query(F.data == "genre_fant")
async def space_movies(callback: types.CallbackQuery):
    movies = db.get_movies_by_category(2)
    if movies:
        response = '\n'.join([f"{movie[1]} - {movie[2]} - {movie[3]} - {movie[4]}" for movie in movies])
    else:
        response = "Список фильмов пуст."
    await callback.message.answer(response)

@start_router.callback_query(F.data == "genre_comedy")
async def space_movies(callback: types.CallbackQuery):
    movies = db.get_movies_by_category(3)
    if movies:
        response = '\n'.join([f"{movie[1]} - {movie[2]} - {movie[3]} - {movie[4]}" for movie in movies])
    else:
        response = "Список фильмов пуст."
    await callback.message.answer(response)

crawler = AnimeSpiritCrawler()

@start_router.callback_query(F.data == "anime")
async def anime_https(callback: types.CallbackQuery):
    links = await crawler.get_anime_data()
    await callback.message.answer(links)

