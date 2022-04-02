from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class IsMat(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        if message.text=='suka':
            return True
        else:
            return False