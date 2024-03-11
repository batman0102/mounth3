import logging
from aiogram import types, Router
from aiogram.filters import Command

myinfo_router = Router()

@myinfo_router.message(Command("myinfo"))
async def myinfo(message: types.Message):
    logging.info(message.from_user)
    await message.answer(f"Ваше имя: {message.from_user.first_name}\nВаш ник: {message.from_user.username}\nВаш айди: {message.from_user.id}")