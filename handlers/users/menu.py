from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardRemove

from keyboards.default import my_key
from loader import dp



@dp.message_handler(Command("menu"))
async def show_m(message: types.Message):
    await message.answer("Сделайте свой выбор", reply_markup=my_key)
@dp.message_handler(text="Мухтар")
async def sey_gav(message: types.Message):
    await message.answer("Gav Ga Gav")

@dp.message_handler(Text(equals=["Лютик","Котя"]))
async def sey_myau(message: types.Message):
    await message.answer("MYAU MYAU MYAU",reply_markup=ReplyKeyboardRemove())