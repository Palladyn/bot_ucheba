from aiogram import Dispatcher

from loader import dp
# from .is_admin import AdminFilter
from .my import  IsMat
from .my2 import IsMat2


if __name__ == "filters":
    dp.filters_factory.bind(IsMat)
    dp.filters_factory.bind(IsMat2)
    pass
