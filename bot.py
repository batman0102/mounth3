from os import getenv
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from db.base import Database


load_dotenv()
bot = Bot(token=getenv("hw1"))
dp = Dispatcher()
db = Database()
