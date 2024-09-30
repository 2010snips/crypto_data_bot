import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("CG_KEY")


# Function to fetch cryptocurrency data
def get_crypto_data(crypto):
    try:
        response = requests.get(
            f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids={crypto}&api_key={api_key}"
        )
        response.raise_for_status()
        data = response.json()[0] if len(response.json()) > 0 else "error"
        return data
    except requests.exceptions.HTTPError as errh:
        print("Http Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Erro connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout error:", errt)
    except requests.exceptions.RequestException as err:
        print("Something went wrong", err)
