import aiohttp, os
from dotenv import load_dotenv

load_dotenv()

bot_key = os.getenv("BOT_KEY")


async def reply_text(chat_id: str, text: str):
    url = f"https://api.telegram.org/bot{bot_key}/sendMessage"

    payload = {
        "chat_id": chat_id,
        "text": text
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload) as response:
            if response.status != 200:
                print(f"Failed to send message. Status code: {response.status}")
