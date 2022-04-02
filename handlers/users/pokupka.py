import logging

from aiogram.dispatcher.filters import Command
from aiogram import types
from aiogram.types import CallbackQuery

from keyboards.inline import in_key
from keyboards.inline.Inline_key import link_key
from keyboards.inline.call_d import buy_call
from loader import dp, bot


@dp.message_handler(Command('menu2'))
async def show_m(message: types.Message):
    await message.answer("Сделайте свой выбор", reply_markup=in_key)

@dp.callback_query_handler(buy_call.filter(iname="AVK"))
async def show_avk(call: CallbackQuery, callback_data: dict):
    logging.info("shag 1")
    # await bot.answer_callback_query(callback_query_id=call.id)
    await call.answer(cache_time=60)
    logging.info(f"call_dat= {call.data}")
    logging.info(f"call_dat_dict= {callback_data}")
    skok = callback_data.get("kolich")
    await call.message.answer(skok,reply_markup=link_key)

@dp.callback_query_handler(text="cancel")
async def cancel(call:CallbackQuery):
    await call.answer("Все пропало" , show_alert=True)
    await call.message.edit_reply_markup()
