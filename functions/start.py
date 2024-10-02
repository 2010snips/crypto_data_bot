from telegram import Update
from telegram.ext import ContextTypes


# command to start the bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    welcome_message = (
        "Hello\\! I am CoinInfoFetch Bot\\. I provide real\\-time data for any cryptocurrency\\.\n\n"
        "*__Commands__*\n"
        "1\\. */data coin* shows info about the coin e\\.g '/data bitcoin'\n\n"
        "2\\. */supply coin* shows the supply of the coin e\\.g '/supply bitcoin'\n\n"
        "3\\. */highlow coin* shows the lowest and highest price of the coin in the last 24 hours e\\.g '/highlow bitcoin'\n\n"
        "4\\. */top10* displays the top 10 cryptocurrencies according to CoinGecko\n\n"
        "*NOTE:* if the coin's name is more than 1 word use \\- to chain the words e\\.g '/data akita\\-inu'"
    )

    await update.message.reply_text(welcome_message, parse_mode="MarkdownV2")
