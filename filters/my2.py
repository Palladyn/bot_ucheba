from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


l=["Хуй", "ХУй", "ХУЙ","хуй","хУй","хУЙ"]
class IsMat2(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        if message.text in l:
            return True
        else:
            return False