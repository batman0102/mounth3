from aiogram import Router, types
from aiogram.filters import Command
from db.base import Database

list_movies = Router()
db = Database()
@list_movies.message(Command("movies"))
async def show_movies(message: types.Message):
    movies = db.get_all_movies()
    if movies:
        response = '\n'.join([f"{movie[1]} - {movie[2]}" for movie in movies])
    else:
        response = "Список фильмов пуст."
    await message.answer(response)
