from telegram import Bot
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.environ.get('TOKEN')
URL = os.environ.get('URL')

bot = Bot(token=TOKEN)

def get_info():
    print(bot.get_webhook_info())


def delete():
    print(bot.delete_webhook())


def set():
    print(bot.set_webhook(url=URL))

set()
