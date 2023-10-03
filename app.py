from dotenv import load_dotenv
import os
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler
import handlers
from flask import Flask, request


load_dotenv()
TOKEN = os.environ.get('TOKEN')

bot = Bot(TOKEN)
dp = Dispatcher(bot, None, workers=0)
app = Flask(__name__)


@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        return '<h1>Webhook is working...!</h1>'

    if request.method == 'POST':
        body = request.get_json()
        
        update = Update.de_json(update, bot)

        dp.add_handler(CommandHandler(['start', 'boshlash'], handlers.start))

        dp.process_update(update)

        return {'message': 'ok'}


if __name__ == '__main__':
    app.run(debug=True)