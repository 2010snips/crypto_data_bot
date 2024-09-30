import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("CG_KEY")


# Function to fetch top 10 cryptocurrencies
def get_top_10_cryptos():
    try:
        response = requests.get(
            f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1&sparkline=false&api_key={api_key}"
        )
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.HTTPError as errh:
        print("Http Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("Something went wrong", err)
