from aiogram import Router
from aiogram.filters import Command
# from aiogram.types import Message, InlineKeyboardButton
# from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.markups.menu_keyboard import menu_keyboard

user_commands_router = Router()

@user_commands_router.message(Command("start"))
async def cmd_start(message: Message):
#     await message.answer("""Добро пожаловать в магазин "Сезон вкусов"!
# Если желаете ознакомиться с ассортиментом, то пришлите команду '/menu'.
# Чтобы сделать заказ, воспользуйтесь кнопкой внизу экрана.""", reply_markup=menu_keyboard)
    await message.answer("""Добро пожаловать в магазин "Сезон вкусов"!
Чтобы сделать заказ, воспользуйтесь кнопкой внизу экрана.""", reply_markup=menu_keyboard)
    
# @user_commands_router.message(Command("menu"))
# async def menu_photo(message: Message):
#     builder = InlineKeyboardBuilder()
#     builder.row(InlineKeyboardButton(
#         text="Пример 1", url="https://disk.yandex.ru/d/qXwBTkZe6rhbIw")
#     )
#     builder.row(InlineKeyboardButton(
#         text="Пример 2",
#         url="https://disk.yandex.ru/d/hkHRy8zdRP_ipw")
#     )

#     await message.answer("Ознакомиться с ассортиментом можно, нажав на одну из кнопок ниже.", reply_markup=builder.as_markup())
