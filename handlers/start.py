from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboadrd import menu
from main import dp


@dp.message_handler((CommandStart()))
async def bot_start(message: types.Message):
    text = f'Привет, {message.from_user.full_name}! ' \
           f'Пришли несколько фотографий, но не более 10'
    await message.answer(text, reply_markup=menu)
