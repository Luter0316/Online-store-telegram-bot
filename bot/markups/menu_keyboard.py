from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types.web_app_info import WebAppInfo

menu_buttons = [
    [KeyboardButton(text="Сделать заказ", web_app=WebAppInfo(url='https://luter0316.github.io/'))]
]
menu_keyboard = ReplyKeyboardMarkup(
    keyboard=menu_buttons,
    resize_keyboard=True)
