from functions.get_top_10_cryptos import get_top_10_cryptos
from telegram import Update
from telegram.ext import ContextTypes

# command to get the highest and lowest prices of a cryptocurrency in the last 24 hours
async def high_low(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # get the crypto name from the message
    crypto = update.message.text.split()[1]
    data = get_top_10_cryptos(crypto)

    if data:
        await update.message.reply_text(
            f'The highest price in the last 24 hours for {crypto} is ${data["high_24h"]}, and the lowest price is ${data["low_24h"]}.'
        )
    else:
        await update.message.reply_text(
            f"Sorry, I could not fetch the data for {crypto}. Please check the cryptocurrency name and try again."
        )
