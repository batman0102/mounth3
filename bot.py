from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
from os import getenv
from db.base import Database
from aiogram.client.session.aiohttp import AiohttpSession


load_dotenv()
session = AiohttpSession(getenv("PROXY_URL"))
bot = Bot(token=getenv("BOT_TOKEN"), session=session)
dp = Dispatcher()
db = Database()

async def on_startup(bot: Bot):
    db.drop_tables()
    db.create_tables()
    db.populate_tables()
    await bot.set_my_commands([
        types.BotCommand(command="/start", description="Начало"),
        types.BotCommand(command="/pic", description="Показать картинку"),
        types.BotCommand(command="/survey", description="Пройти опрос"),
        types.BotCommand(command="/myinfo", description="Информация обо мне")
    ])