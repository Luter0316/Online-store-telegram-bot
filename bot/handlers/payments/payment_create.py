import yookassa
from yookassa import Payment
import uuid
import config

yookassa.Configuration.account_id = config.ACCOUNT_ID
yookassa.Configuration.secret_key = config.SECRET_KEY

def create(amount, chat_id):
    id_key = str(uuid.uuid4())
    payment = Payment.create({
        "amount": {
            'value': amount,
            'currency': "RUB"
        },
        'payment_method_data': {
            'type': 'bank_card'
        },
        'confirmation': {
            'type': 'redirect',
            'return_url': 'https://t.me/SezonVkusov_bot'
        },
        'capture': True,
        'metadata': {
            'chat_id': chat_id
        },
        'description': 'РЕАЛИЗОВАТЬ ИМПОРТ ЗАКАЗА'
    }, id_key)

    return payment.confirmation.confirmation_url, payment.id
