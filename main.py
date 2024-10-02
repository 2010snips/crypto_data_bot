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

load_dotenv()

bot_key = os.getenv("BOT_KEY")

app = Flask(__name__)

# Create Telegram application
application = ApplicationBuilder().token(bot_key).build()

# Command handlers
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("data", data))
application.add_handler(CommandHandler("highlow", high_low))
application.add_handler(CommandHandler("supply", supply))
application.add_handler(CommandHandler("top10", display_top_10_cryptos))


@app.route("/", methods=["POST"])

def webhook():
    update = Update.de_json(request.get_json(force=True), application.bot)
    application.update_queue.put([update])
    return "ok"


if __name__ == "__main__":
    application.bot.set_webhook(url="https://sweet-ronica-eniitan-be83931d.koyeb.app/")

    app.run(host="0.0.0.0", port=8000)
