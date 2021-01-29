import logging

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor

from config import BOT_TOKEN, ADMINS

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


async def on_startup(dp: Dispatcher):
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, 'Бот запущен')
        except Exception as err:
            logging.exception(err)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
