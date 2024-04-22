import json

from aiogram import Router, F
from aiogram.types import Message, web_app_data

ru_product_dict = {
    'BananaStrips': 'Банановые фрипсы',
    'PearStrips': 'Грушевые фрипсы',
    'KiwiStrips': ' Киви фрипсы',
    'MangoStrips': 'Манго фрипсы'
}

pay_router = Router()

@pay_router.message(F.web_app_data)
async def payment(message: Message):
    json_data = message.web_app_data.data
    parsed_data = json.loads(json_data)
    order_message = ""
    for i, item in enumerate(parsed_data['items'], start=1):
        position = ru_product_dict[item['id']]
        # position = int(item['id'].replace('item', ''))
        order_message += f"Позиция {position}\n"
        order_message += f"Стоимость: {item['price']}\n\n"


    order_message += f"Общая стоимость товаров: {parsed_data['totalPrice']}"


    await message.answer(f"""
{order_message}
""")
    
#     await message.answer('ID админского чата', f"""
# Новый заказ

# {message}
#     """)
