import asyncio # Асинхронность
import logging # Логирование всех действий (помощь в отладке)

from aiogram import Bot, Dispatcher # Библиотека бота
from aiogram.enums.parse_mode import ParseMode # Настройки разметки сообщений (HTML, Markdown)
from aiogram.fsm.storage.memory import MemoryStorage # Хранилища данных для состояний пользователей

from bot.handlers.user import commands # Команды пользователей
from bot.handlers.orders import order_handler
import config # Настройки бота


# Непрерывная функция обработки входящих запросов
async def main() -> None:
    bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage()) # Все несохраненные данные в БД, будут стёрты при перезапуске
    dp.include_routers(commands.user_commands_router, order_handler.order_router)

    await bot.delete_webhook(drop_pending_updates=True) # Удаляет все обновления, которые произошли после последнего завершения работы бота
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


# Запуск бота
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
