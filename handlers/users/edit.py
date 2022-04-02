from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.edited_message_handler()
async def tst(message: types.Message):
    await message.reply(f"Внесена правка")
