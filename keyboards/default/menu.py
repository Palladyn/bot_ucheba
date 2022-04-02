from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

my_key=ReplyKeyboardMarkup([
    [
       KeyboardButton(text="Мухтар")
    ],
    [

        KeyboardButton(text="Лютик"),
        KeyboardButton(text="Котя")
    ]

], resize_keyboard=True)