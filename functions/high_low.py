from functions.get_crypto_data import get_crypto_data
from functions.reply_text import reply_text


def high_low(chat_id: str, crypto: str) -> None:
    data: dict = get_crypto_data(crypto)

    if data:
        reply_text(
            chat_id,
            f'The highest price in the last 24 hours for {crypto} is ${data["high_24h"]}, and the lowest price is ${data["low_24h"]}.',
        )
    else:
        reply_text(chat_id, f"Sorry, data on {crypto} isn't available right now")
