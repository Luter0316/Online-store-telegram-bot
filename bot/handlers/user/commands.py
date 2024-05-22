from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from bot.markups.menu_keyboard import menu_keyboard

user_commands_router = Router()

@user_commands_router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("""Добро пожаловать в магазин "Сезон вкусов"!""", reply_markup=menu_keyboard)
