from aiogram import Router, types
from aiogram.filters import Command
from bot import db

list_movies = Router()

@list_movies.message(Command("list"))
async def show_movies(message: types.Message):
    movies = db.get_all_movies()
    if movies:
        response = '\n'.join([f"{movie[1]} - {movie[2]} - {movie[3]}" for movie in movies])
    else:
        response = "Список фильмов пуст."
    await message.answer(response)
