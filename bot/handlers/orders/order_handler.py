import json

from aiogram import Router, F
from aiogram.types import Message, web_app_data, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import Bot
from random import randint

from bot.handlers.payments.payment_create import create

ru_product_dict = {
    'BananaStrips': 'Банановые фрипсы',
    'AppleStrips': 'Яблочные фрипсы',
    'PearStrips': 'Грушевые фрипсы',
    'KiwiStrips': 'Киви фрипсы',
    'OrangeStrips': 'Апельсиновые фрипсы',
    'PineappleStrips': 'Ананасовые фрипсы',
    'MangoStrips': 'Манговые фрипсы',
    'BananaInCoconutStrips': 'Банан в кокосе фрипсы',
    'PersimmonStrips': 'Хурма фрипсы',
    'CoconutStrips': 'Кокосовые фрипсы'
}

order_router = Router()

@order_router.message(F.web_app_data)
async def order(message: Message, bot: Bot):
    json_data = message.web_app_data.data
    parsed_data = json.loads(json_data)
    order_message = ""
    for i, item in enumerate(parsed_data['items'], start=1):
        position = ru_product_dict[item['id']]
        # position = int(item['id'].replace('item', ''))
        order_message += f"Позиция {position}\n"
        order_message += f"Стоимость: {item['price']}\n\n"


    order_message += f"Общая стоимость товаров: {parsed_data['totalPrice']}"
    pay_url, payment_id = create(parsed_data['totalPrice'], message.chat.id, order_message[:100])#лимит на длину описания

    # Клавиатура
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(
        text="Оплатить", 
        url= pay_url
    ))

    order_number = create_order_number(payment_id, parsed_data['totalPrice'])
    #Отправка сообщения в админский чат
    await bot.send_message(928752105, f"""Номер платежа: {payment_id}
# Новый заказ! {order_number}
# {order_message}
#     """)
    
    await message.answer(f"Номер вашего заказа: {order_number} \n{order_message}", reply_markup=builder.as_markup())

def create_order_number(id: str, price):
    order_id = randint(0, 100)
    for i in range(len(id)):
        if id[i].isdigit():
            order_id += int(id[i]) 
    return order_id
