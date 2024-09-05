from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
but = ReplyKeyboardMarkup(
       keyboard=[
           [KeyboardButton("Ulashish", request_contact=True)]
       ],
       resize_keyboard=True
)  


but1 = ReplyKeyboardMarkup(
       keyboard=[
           [KeyboardButton("Shikoyat yaratish")],
           [KeyboardButton("Shikoyat ko'rish")]
       ],
       resize_keyboard=True
)  


but2 = ReplyKeyboardMarkup(
       keyboard=[
        [   KeyboardButton("MARS"),
            KeyboardButton("Uzinfacom"),
            KeyboardButton("Realsoft"),
            KeyboardButton("Smartsoft"),
            KeyboardButton("Cloudit")],
           [KeyboardButton("Pentagon"),
           KeyboardButton("UIC group"),
           KeyboardButton("Cometa"),
           KeyboardButton("MXX"),
           KeyboardButton("YPX")]
       ],
       resize_keyboard=True
)   


location = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton('lokatsiya', request_location = True)]
    ],
    resize_keyboard = True,
)

but3 = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("Shikoyat ko'rish")]
    ],
    resize_keyboard=True
)

