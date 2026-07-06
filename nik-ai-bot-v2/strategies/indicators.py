"""
=========================================================
NIKHIL AI FOREX BOT V2.0
Technical Indicators
=========================================================
"""

from ta.trend import EMAIndicator, MACD, ADXIndicator
from ta.momentum import RSIIndicator
from ta.volatility import BollingerBands, AverageTrueRange


def calculate_indicators(df):

    close = df["close"]
    high = df["high"]
    low = df["low"]
    open_price = df["open"]

    # EMA
    df["ema9"] = EMAIndicator(close=close, window=9).ema_indicator()
    df["ema21"] = EMAIndicator(close=close, window=21).ema_indicator()
    df["ema50"] = EMAIndicator(close=close, window=50).ema_indicator()
    df["ema200"] = EMAIndicator(close=close, window=200).ema_indicator()

    # RSI
    df["rsi"] = RSIIndicator(close=close, window=14).rsi()

    # MACD
    macd = MACD(close=close)

    df["macd"] = macd.macd()
    df["macd_signal"] = macd.macd_signal()
    df["macd_hist"] = macd.macd_diff()

    # Bollinger
    bb = BollingerBands(close=close)

    df["bb_upper"] = bb.bollinger_hband()
    df["bb_middle"] = bb.bollinger_mavg()
    df["bb_lower"] = bb.bollinger_lband()

    # ATR
    atr = AverageTrueRange(
        high=high,
        low=low,
        close=close
    )

    df["atr"] = atr.average_true_range()

    # ADX
    adx = ADXIndicator(
        high=high,
        low=low,
        close=close
    )

    df["adx"] = adx.adx()

    # Candle body
    df["body"] = abs(df["close"] - df["open"])

    # Trend
    df["trend"] = "SIDEWAYS"

    df.loc[
        (df["ema9"] > df["ema21"]) &
        (df["ema21"] > df["ema50"]),
        "trend"
    ] = "UP"

    df.loc[
        (df["ema9"] < df["ema21"]) &
        (df["ema21"] < df["ema50"]),
        "trend"
    ] = "DOWN"

    return df
