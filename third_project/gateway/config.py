import os

TOKEN = os.environ.get('TELEGRAM_TOKEN', '123:abc')
CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID', '')
PORT = 8080

ROUTES = {
    'ci': ['telegram', 'console'],
    'crm': ['console'],
}
