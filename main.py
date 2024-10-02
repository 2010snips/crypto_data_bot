from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler
from dotenv import load_dotenv
import os
from functions.start import start
from functions.data import data
from functions.high_low import high_low
from functions.supply import supply
from functions.display_top_10_cryptos import display_top_10_cryptos
from flask import Flask, request
from dotenv import load_dotenv
import asyncio
import requests

load_dotenv()

bot_key = os.getenv("BOT_KEY")

app = Flask(__name__)

# Create Telegram application
application = ApplicationBuilder().token(bot_key).build()


def replyText(chat_id, text):
    url = f"https://api.telegram.org/bot{bot_key}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    response = requests.post(url, json=payload)
    return response


def message_parser(message):
    chat_id = message["message"]["chat"]["id"]
    text = message["message"]["text"]
    print(f"message: {text}")
    return chat_id, text


# Command handlers
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("data", data))
application.add_handler(CommandHandler("highlow", high_low))
application.add_handler(CommandHandler("supply", supply))
application.add_handler(CommandHandler("top10", display_top_10_cryptos))


@app.route("/webhook", methods=["POST"])
async def webhook():
    json_data = request.get_json()
    chat_id, text = message_parser(json_data)
    if text == "/start":
        replyText(chat_id, "Hi from Eniitan")
    else:
        replyText(chat_id, text)
    return "ok"


# async def webhook():
#     print("recieved")
#     json_data = request.get_json(force=True)
#     update = Update.de_json(json_data, application.bot)
#     await application.update_queue.put(update)
#     return "ok"
