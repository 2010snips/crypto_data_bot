import requests, os
from dotenv import load_dotenv

load_dotenv()

bot_key = os.getenv("BOT_KEY")

def reply_text(chat_id: str, text: str):
    url = f"https://api.telegram.org/bot{bot_key}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, json=payload)
