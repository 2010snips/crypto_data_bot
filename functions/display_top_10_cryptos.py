from functions.get_top_10_cryptos import get_top_10_cryptos
from telegram import Update
from telegram.ext import ContextTypes


# command to get the top 10 cryptocurrencies
async def display_top_10_cryptos(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    data = get_top_10_cryptos()
    if data and data != "error":
        message = "Here are the top 10 cryptocurrencies according to CoinGecko:\n"
        for i, crypto in enumerate(data, start=1):
            message += f'{i}. *{crypto["name"]}* ({crypto["symbol"].upper()}):\n- Current price is ${crypto["current_price"]}\n- Market cap is ${crypto["market_cap"]}\n- Total volume in the last 24 hours is ${crypto["total_volume"]}\n\n'
        await update.message.reply_text(message, parse_mode="Markdown")
    elif data == "error":
        await update.message.reply_text(
            f"Sorry, data on the top10 cryptocurrencies isn't available right now"
        )
    else:
        await update.message.reply_text(
            "Sorry, I could not fetch the data for the top 10 cryptocurrencies. Please try again later."
        )
