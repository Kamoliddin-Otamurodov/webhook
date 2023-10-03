from dotenv import load_dotenv
import os
from telegram.ext import Updater, CommandHandler
import handlers


load_dotenv()
TOKEN = os.environ.get("TOKEN")


def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler(['start', 'boshlash'], handlers.start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()