from functions.get_crypto_data import get_crypto_data
from telegram import Update
from telegram.ext import ContextTypes


# command to get the highest and lowest prices of a cryptocurrency in the last 24 hours
async def high_low(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # get the crypto name from the message
    crypto: str = update.message.text.split()[1]
    data: dict = get_crypto_data(crypto)

    if data:
        await update.message.reply_text(
            f'The highest price in the last 24 hours for {crypto} is ${data["high_24h"]}, and the lowest price is ${data["low_24h"]}.'
        )
    else:
        await update.message.reply_text(
            f"Sorry, data on {crypto} isn't available right now"
        )
