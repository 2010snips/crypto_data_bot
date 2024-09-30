from telegram.ext import ApplicationBuilder, CommandHandler
from dotenv import load_dotenv
import os
from functions.start import start
from functions.data import data
from functions.high_low import high_low
from functions.supply import supply
from functions.display_top_10_cryptos import display_top_10_cryptos

load_dotenv()

bot_key = os.getenv("BOT_KEY")

app = ApplicationBuilder().token(bot_key).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("data", data))
app.add_handler(CommandHandler("high_low", high_low))
app.add_handler(CommandHandler("supply", supply))
app.add_handler(CommandHandler("top10", display_top_10_cryptos))

app.run_polling()
