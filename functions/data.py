from functions.get_crypto_data import get_crypto_data
from functions.reply_text import reply_text


async def data(chat_id: str, crypto: str) -> None:
    data = await get_crypto_data(crypto)

    if data:
        await reply_text(
            chat_id,
            f'*The current price of {crypto} is ${data["current_price"]}*. The price change in the last 24 hours is {data["price_change_percentage_24h"]}%.\nThe market cap is ${data["market_cap"]}.\nThe total volume in the last 24 hours is ${data["total_volume"]}.',
        )
    else:
        await reply_text(chat_id, f"Sorry, data on {crypto} isn't available right now")
