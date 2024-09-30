from get_crypto_data import get_crypto_data
from telegram import Update
from telegram.ext import ContextTypes

# command to get the circulating and total supply of a cryptocurrency
async def supply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # get the crypto name from the message
    crypto = update.message.text.split()[1]
    data = get_crypto_data(crypto)

    if data:
        await update.message.reply_text(
            f'The circulating supply of {crypto} is {data["circulating_supply"]}, and the total supply is {data["total_supply"]}.'
        )
    else:
        await update.message.reply_text(
            f"Sorry, I could not fetch the data for {crypto}. Please check the cryptocurrency name and try again."
        )