import asyncio
import logging
from aiogram import Bot

from bot import dp,bot, db
from handlers.start import start_router
from handlers.myinfo import myinfo_router
from handlers.random_pic import pic_router
from handlers.survey import survey_router
from handlers.list_movies import list_movies

async def on_startup(bot: Bot):
    db.drop_tables()
    db.create_tables()
    db.populate_tables()

async def main():
    dp.include_router(start_router)
    dp.include_router(myinfo_router)
    dp.include_router(pic_router)
    dp.include_router(survey_router)
    dp.include_router(list_movies)
    dp.startup.register(on_startup)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
