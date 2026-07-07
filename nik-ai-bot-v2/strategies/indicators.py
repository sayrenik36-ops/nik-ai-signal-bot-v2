import pandas as pd
import pandas_ta as ta


class IndicatorEngine:

    @staticmethod
    def calculate(df):

        df = df.copy()

        # EMA
        df["ema20"] = ta.ema(df["close"], length=20)
        df["ema50"] = ta.ema(df["close"], length=50)
        df["ema200"] = ta.ema(df["close"], length=200)

        # RSI
        df["rsi"] = ta.rsi(df["close"], length=14)

        # MACD
        macd = ta.macd(df["close"])

        df["macd"] = macd["MACD_12_26_9"]
        df["macd_signal"] = macd["MACDs_12_26_9"]

        # ADX
        adx = ta.adx(
            high=df["high"],
            low=df["low"],
            close=df["close"]
        )

        df["adx"] = adx["ADX_14"]

        # ATR
        df["atr"] = ta.atr(
            high=df["high"],
            low=df["low"],
            close=df["close"]
        )

        # Bollinger Bands
        bb = ta.bbands(df["close"])

        df["bb_upper"] = bb["BBU_20_2.0"]
        df["bb_lower"] = bb["BBL_20_2.0"]

        return df