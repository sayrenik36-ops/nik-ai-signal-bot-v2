"""
=========================================================
NIKHIL AI FOREX BOT V2.0
Market Data Service
=========================================================
"""

from twelvedata import TDClient
import pandas as pd

from config import (
    API_KEY,
    TIMEFRAME,
    OUTPUT_SIZE,
)

# Create TwelveData client
td = TDClient(apikey=API_KEY)


def get_market_data(symbol):
    """
    Download OHLC data from TwelveData
    """

    try:

        ts = td.time_series(
            symbol=symbol,
            interval=TIMEFRAME,
            outputsize=OUTPUT_SIZE,
        )

        df = ts.as_pandas()

        if df is None or df.empty:
            print(f"[ERROR] No data received for {symbol}")
            return None

        # TwelveData returns newest first
        df = df.iloc[::-1].copy()

        # Convert columns to float
        numeric_columns = [
            "open",
            "high",
            "low",
            "close",
        ]

        for col in numeric_columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

        # Remove invalid rows
        df.dropna(inplace=True)

        if len(df) < 60:
            print(f"[ERROR] Not enough candles for {symbol}")
            return None

        return df

    except Exception as e:

        print("=" * 60)
        print("MARKET DATA ERROR")
        print(f"Pair : {symbol}")
        print(f"Error: {e}")
        print("=" * 60)

        return None