from telegram import Update
from telegram.ext import ContextTypes


# command to start the bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    welcome_message = "Hello! I am your Crypto Bot. I can provide real-time data for any cryptocurrency. Use /data <crypto-name> to get started\n Example: /data bitcoin."

    await update.message.reply_text(welcome_message)
