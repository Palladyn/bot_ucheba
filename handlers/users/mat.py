from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from filters import IsMat

@dp.message_handler(IsMat())
async def tst(message: types.Message):
    await message.answer(f"Не Матерись")