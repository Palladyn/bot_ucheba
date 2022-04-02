from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(text='tst')
async def tst(message: types.Message):
    await message.answer(f"Привет, tost")
