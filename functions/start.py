from functions.reply_text import reply_text


async def start(chatId: str) -> None:
    welcome_message = (
        "Hello! I am CoinInfoFetch Bot\\. I provide real\\-time data for any cryptocurrency\\.\n\n"
        "*__Commands__*\n"
        "1\\. */data coin* shows info about coin e\\.g\\., /data bitcoin\n"
        "2\\. */supply coin* shows the supply of the coin e\\.g\\., /supply bitcoin\n"
        "3\\. */highlow coin* shows the lowest and highest price of the coin in the last 24 hours e\\.g\\., /highlow bitcoin\n"
        "4\\. */top10* displays the top 10 cryptocurrencies according to CoinGecko\n\n"
        "*NOTE:* if the coin's name is more than 1 word, use '-' to chain the words e.g. '/data akita-inu'"
    )

    await reply_text(chatId, welcome_message)
