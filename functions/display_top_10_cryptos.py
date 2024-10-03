from functions.get_top_10_cryptos import get_top_10_cryptos
from functions.reply_text import reply_text


async def display_top_10_cryptos(chat_id: str) -> None:
    data: list = await get_top_10_cryptos()

    if data:
        message = "*Here are the top 10 cryptocurrencies according to CoinGecko:*\n\n"
        for i, crypto in enumerate(data, start=1):
            message += (
                f'{i}\. *{crypto["name"].replace("-", "\\-")}* '
                f'\\({crypto["symbol"].upper().replace("-", "\\-")}\\):\n'
                f'- Current price is \\${crypto["current_price"]}\n'
                f'- Market cap is \\${crypto["market_cap"]}\n'
                f'- Total volume in the last 24 hours is \\${crypto["total_volume"]}\n\n'
            )
        await reply_text(chat_id, message)
    else:
        await reply_text(
            chat_id,
            "Sorry, I could not fetch the data for the top 10 cryptocurrencies. Please try again later.",
        )
