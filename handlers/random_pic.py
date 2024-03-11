import os
import random
from aiogram import types, Router
from aiogram.filters import Command

pic_router = Router()

@pic_router.message(Command("random_pic"))
async def send_random_pic(message: types.Message):
    images_folder = 'images'
    random_image_name = random.choice(os.listdir(images_folder))
    file_path = os.path.join(images_folder, random_image_name)
    file = types.FSInputFile(file_path)
    await message.answer_photo(file)