import os
from dotenv import load_dotenv

# Создание переменных окружения
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

BOT_TOKEN = os.getenv('BOT_TOKEN')
ACCOUNT_ID = os.getenv('ACCOUNT_ID')
SECRET_KEY = os.getenv('SECRET_KEY')
