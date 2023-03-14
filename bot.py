import os
from aiogram.dispatcher.filters import Text
import logic

from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton, KeyboardButton
from dotenv import load_dotenv

load_dotenv()

# API key
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot)

user_values = {}


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton(text="Choose car")
    keyboard.add(button)
    with open(f'car_bot.png', 'rb') as photo:
        await message.answer_photo(photo=photo, caption="Hello, i'm car bot.\nI will help you to choose a car 🚗",
                                   reply_markup=keyboard)


@dp.message_handler(Text(equals="Choose car"))
async def send_welcome(message: types.Message):
    buttons = [
        InlineKeyboardButton(text="Sport", callback_data="car_type_sport"),
        InlineKeyboardButton(text="Comfort", callback_data="car_type_comfort"),
        InlineKeyboardButton(text="Off-road", callback_data="car_type_off_road")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.answer("What type of car do you want: ", reply_markup=keyboard)


@dp.callback_query_handler(Text(startswith="car_type_"))
async def callbacks_taste(call: types.CallbackQuery):
    action = call.data
    if action == "car_type_sport":
        user_values['car_type_val'] = 28
    elif action == "car_type_comfort":
        user_values['car_type_val'] = 56
    elif action == "car_type_off_road":
        user_values['car_type_val'] = 78
    buttons = [
        InlineKeyboardButton(text="Petrol", callback_data="engine_petrol"),
        InlineKeyboardButton(text="Electro", callback_data="engine_electro"),
        InlineKeyboardButton(text="Hybrid", callback_data="engine_hybrid")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await call.message.edit_text(text='What type of engine do you prefer: ', reply_markup=keyboard)
    await call.answer()


@dp.callback_query_handler(Text(startswith="engine_"))
async def callbacks_taste(call: types.CallbackQuery):
    action = call.data
    if action == "engine_petrol":
        user_values['engine_val'] = 2
    elif action == "engine_electro":
        user_values['engine_val'] = 4
    elif action == "engine_hybrid":
        user_values['engine_val'] = 8
    buttons = [
        InlineKeyboardButton(text="10000$", callback_data="price_low"),
        InlineKeyboardButton(text="30000$", callback_data="price_mid"),
        InlineKeyboardButton(text="100000$", callback_data="price_high")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await call.message.edit_text(text='Your budget (under): ', reply_markup=keyboard)
    await call.answer()


@dp.callback_query_handler(Text(startswith="price_"))
async def callbacks_taste(call: types.CallbackQuery):
    action = call.data
    if action == "price_low":
        user_values['price_val'] = 25
    elif action == "price_mid":
        user_values['price_val'] = 56
    elif action == "price_high":
        user_values['price_val'] = 87
    await call.message.edit_text(text=f'Your car:')
    caption = logic.fuzzy_logic(**user_values)
    with open(f'car_img/{caption}.jpg', 'rb') as photo:
        await call.message.answer_photo(photo=photo, caption=caption)
    await call.answer()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
