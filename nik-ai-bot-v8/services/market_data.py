import requests
import pandas as pd
from config import API_KEY


def get_price(symbol="EUR/USD"):

    url = (
        "https://api.twelvedata.com/price"
        f"?symbol={symbol}"
        f"&apikey={API_KEY}"
    )

    try:

        response = requests.get(
            url,
            timeout=10
        )

        data = response.json()

        if "price" in data:
            return float(data["price"])

        print(
            "API Error:",
            data
        )

        return None


    except Exception as e:

        print(
            "Market data error:",
            e
        )

        return None



def get_candles(
        symbol="EUR/USD",
        interval="1min",
        outputsize=50
):

    url = (
        "https://api.twelvedata.com/time_series"
        f"?symbol={symbol}"
        f"&interval={interval}"
        f"&outputsize={outputsize}"
        f"&apikey={API_KEY}"
    )


    try:

        response = requests.get(
            url,
            timeout=10
        )

        data = response.json()


        if "values" not in data:

            print(
                "API Error:",
                data
            )

            return None


        df = pd.DataFrame(
            data["values"]
        )


        df = df.rename(
            columns={
                "datetime": "time"
            }
        )


        for col in [
            "open",
            "high",
            "low",
            "close"
        ]:

            df[col] = df[col].astype(float)


        df = df.iloc[::-1]


        return df


    except Exception as e:

        print(
            "Candle error:",
            e
        )

        return None
