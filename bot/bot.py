from buttons import *
from datetime import datetime
from sql import *
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardRemove
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = '7458244150:AAH-1A4qCNwBU3GPguBVbjTNrN45pjh3bgc'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
storage = MemoryStorage()
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)
dp.middleware.setup(LoggingMiddleware())


class Buyruqlar(StatesGroup):
    nomer = State()
    ism = State()

class Shikoyat(StatesGroup):
    manzil = State()
    shikoyat = State()
    tashkilot = State()
    check_in = State()
    yaratish = State()
    korish = State()


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu alaykum Shikoyat botiga xush kelibsiz)")
    await message.answer('Ismingizni kiriting!')
    await Buyruqlar.ism.set()


@dp.message_handler(state = Buyruqlar.ism)
async def terl(msg: types.Message, state: FSMContext):
    global ism
    ism = msg.text
    await state.finish()
    await Buyruqlar.nomer.set()
    await msg.answer("Nomeringizni kiriting!: ")


@dp.message_handler(state = Buyruqlar.nomer)
async def terl(msg: types.Message, state: FSMContext):
    global nomer
    nomer = msg.text
    if nomer.isdigit() and len(nomer)==9:
        u = user(ism, nomer)
        await msg.answer(f'{u}')
        await state.finish()
        await msg.answer("Tanlang!:", reply_markup=but1)
    else:
        await msg.answer("Noto'g'ri nomer kiritdingiz!")
        await Buyruqlar.nomer.set()


@dp.message_handler(text = 'Shikoyat yaratish')
async def terl(msg: types.Message, state = FSMContext):
    await state.finish()
    await Shikoyat.manzil.set()
    await msg.answer("Manzilingiz:", reply_markup=location) 


@dp.message_handler(content_types=types.ContentType.LOCATION, state = Shikoyat.manzil)
async def z(msg: types.Message, state = FSMContext):
    global manzil
    manzil = msg.location
    print(manzil)
    await state.finish()
    await Shikoyat.tashkilot.set()
    await msg.answer('Lokatsiya olindi \nTashkilotni tanlang!', reply_markup=but2)
    



@dp.message_handler(state = Shikoyat.tashkilot)
async def terl(msg: types.Message, state: FSMContext):
    global tashkilot
    tashkilot = msg.text
    await state.finish()
    await Shikoyat.yaratish.set()
    await msg.answer("Shikoyatingizni yozing: ")


@dp.message_handler(state = Shikoyat.yaratish)
async def terl(msg: types.Message, state: FSMContext):
    shikoyat = msg.text   
    holat = 'NULL'
    id = msg.from_user.id
    await state.finish()
    s = shikoyatlar(id, manzil, tashkilot, shikoyat, holat)
    await msg.answer("Shikoyatingiz qabul qilindi!", reply_markup=but3)







@dp.message_handler(text="Shikoyat ko'rish")
async def shikoyat(msg: types.Message):
    id = msg.from_user.id
    all = get_shikoyat(id)
    natija = ''
    tashkilot = []
    holat = []
    for i in all:
        tashkilot.append(i[2])
        if i[-1] == "NULL":
            holat.append("   ")
        else:
            holat.append(i[-1])
    
    keyboard = InlineKeyboardMarkup(row_width=1)  # create an inline keyboard
    
    for i in range(len(tashkilot)):
        s = f"{tashkilot[i]} --- {holat[i]}\n"
        natija += s
        button = InlineKeyboardButton(text=tashkilot[i], callback_data=f"shikoyat_{tashkilot[i]}")
        keyboard.add(button)
    
    await msg.answer(f"{natija}")
    await msg.answer(reply_markup=ReplyKeyboardRemove())
    await msg.answer("Shikoyatingizni tanlang!", reply_markup=keyboard)

# Handle button press
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('shikoyat_'))
async def process_shikoyat_button(callback_query: types.CallbackQuery):
    index = callback_query.data.split('_')[1]
    shikoyat = get_one_shikoyat(index)
    # You can do further processing based on the selected organization
    await callback_query.message.answer(text = f'{s}')
    # await callback_query.answer()







if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
    con.close()