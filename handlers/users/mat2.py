import logging

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, bot
from filters import IsMat, IsMat2

l=["Хуй", "ХУй", "ХУЙ","хуй","хУй","хУЙ"]
# @dp.message_handler(regexp='[Х]|[х][У]|[у][Й]|[й]')# фраза содержит слово
@dp.message_handler (IsMat2() )
async def del_mes(message: types.Message):
    # await bot.delete_message(message.chat.id,message.message_id)
    await message.delete()
    await message.answer(f" Уважаемый {message.from_user.full_name} Говори культурно")
    await bot.kick_chat_member(user_id=message.from_user.id,chat_id=message.chat.id)
    # logging.info()
@dp.message_handler(content_types=types.ContentType.LEFT_CHAT_MEMBER)
async def ban_r(message: types.Message):
    await message.answer(f" user {message.left_chat_member.full_name}  получил бан")
