from functions.get_crypto_data import get_crypto_data
from functions.reply_text import reply_text


async def supply(chat_id: str, crypto) -> None:
    data = await get_crypto_data(crypto)

    if data:
        await reply_text(
            chat_id,
            f'The circulating supply of {crypto} is {data["circulating_supply"]}, and the total supply is {data["total_supply"]}.',
        )
    else:
        await reply_text(chat_id, f"Sorry, data on {crypto} isn't available right now")
