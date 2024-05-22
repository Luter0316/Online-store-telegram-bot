
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton


from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types.web_app_info import WebAppInfo

assortment_buttons = [
    [KeyboardButton(text="Ознакомиться с товарным видом", url='https://disk.yandex.ru/d/qXwBTkZe6rhbIw')]
]
assortment_keyboard = InlineKeyboardMarkup(
    keyboard=assortment_buttons)
