import asyncio
import os
import random
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv
from os import  getenv
import logging

load_dotenv()
bot = Bot(token=getenv("hw1"))
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: types.Message):
    logging.info(message.from_user)
    await message.answer(f"Привет, {message.from_user.first_name}")

@dp.message(Command("myinfo"))
async def echo(message: types.Message):
    logging.info(message.from_user)
    await message.answer(f"Ваше имя: {message.from_user.first_name}\nВаш ник: {message.from_user.username}\nВаш айди: {message.from_user.id}")


@dp.message(Command("random_pic"))
async def send_random_pic(message: types.Message):
    images_folder = 'images'
    random_image_name = random.choice(os.listdir(images_folder))
    file_path = os.path.join(images_folder, random_image_name)
    file = types.FSInputFile(file_path)
    await message.answer_photo(file)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

