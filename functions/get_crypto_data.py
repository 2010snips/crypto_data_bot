from dotenv import load_dotenv
import os
import aiohttp

load_dotenv()

api_key = os.getenv("CG_KEY")


async def get_crypto_data(crypto: str) -> dict | None:
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids={crypto}&api_key={api_key}"
            ) as response:
                response.raise_for_status()

                data: dict = await response.json()[0]

                # because sometimes it returns an empty list
                if data:
                    return data
                else:
                    raise Exception()
    except aiohttp.ClientResponseError as err:
        print(f"HTTP Error: {err.status} - {err.message}")
    except aiohttp.ClientError as err:
        print("Client Error:", err)
    except Exception as err:
        print("Something went wrong:", err)
