from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.call_d import buy_call


in_key=InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [
        InlineKeyboardButton( text= "Рошен",callback_data=buy_call.new(iname='roshen',kolich=1)),
        InlineKeyboardButton(text="АВК",callback_data="buy:AVK:3")

    ],
    [
        InlineKeyboardButton(
            text="cancel",
            callback_data="cancel"
        )
    ]
])
link_key=InlineKeyboardMarkup()
Link="https://korrespondent.net/"
link_k=InlineKeyboardButton(text="купить",url=Link)
link_key.insert(link_k)