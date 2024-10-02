import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("CG_KEY")


# Function to fetch cryptocurrency data
def get_crypto_data(crypto: str) -> dict | None:
    try:
        response = requests.get(
            f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids={crypto}&api_key={api_key}"
        )
        response.raise_for_status()

        data: dict = response.json()[0]

        # because sometimes it returns an empty list
        if data:
            return data
        else:
            raise Exception()
    except requests.exceptions.HTTPError as errh:
        print("Http Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout error:", errt)
    except (requests.exceptions.RequestException, Exception) as err:
        print("Something went wrong", err)
