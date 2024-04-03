import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

# Создание переменных окружения
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

# Непрерывная функция обработки входящих запросов
async def main():
    bot = Bot(token="TOKEN")
    dp = Dispatcher()

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

# Запуск бота
if __name__ == "__main__":
    asyncio.run(main())
