from telegram import Update
from telegram.ext import ContextTypes
from functions.get_crypto_data import get_crypto_data


# command to get the data of a coin or token
async def data(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # get the crypto name from the message
    crypto = update.message.text.split()[1]
    data = get_crypto_data(crypto)

    if data and data != "error":
        await update.message.reply_text(
            f'The current price of {crypto} is ${data["current_price"]}. The price change in the last 24 hours is {data["price_change_percentage_24h"]}%.\nThe market cap is ${data["market_cap"]}.\nThe total volume in the last 24 hours is ${data["total_volume"]}.'
        )
    elif data == "error":
        await update.message.reply_text(
            f"Sorry, data on {crypto} isn't available right now"
        )
    else:
        await update.message.reply_text(
            f"Sorry, I could not fetch the data for {crypto}. Please check the cryptocurrency name and try again."
        )
