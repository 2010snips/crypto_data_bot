import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("CG_KEY")


def get_top_10_cryptos() -> list | None:
    try:
        response = requests.get(
            f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1&sparkline=false&api_key={api_key}"
        )
        response.raise_for_status()

        data: list = response.json()

        # because sometimes it returns an empty list
        if data:
            return data
        else:
            raise Exception()

    except requests.exceptions.HTTPError as errh:
        print("Http Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except (requests.exceptions.RequestException, Exception) as err:
        print("Something went wrong", err)
