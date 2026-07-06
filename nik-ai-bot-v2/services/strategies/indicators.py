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
    """
    Calculate all technical indicators used by the AI strategy.
    """

    close = df["close"]
    high = df["high"]
    low = df["low"]
    open_price = df["open"]

    # ==========================
    # EMA
    # ==========================

    df["ema9"] = EMAIndicator(close=close, window=9).ema_indicator()
    df["ema21"] = EMAIndicator(close=close, window=21).ema_indicator()
    df["ema50"] = EMAIndicator(close=close, window=50).ema_indicator()
    df["ema200"] = EMAIndicator(close=close, window=200).ema_indicator()

    # ==========================
    # RSI
    # ==========================

    df["rsi"] = RSIIndicator(close=close, window=14).rsi()

    # ==========================
    # MACD
    # ==========================

    macd = MACD(close=close)

    df["macd"] = macd.macd()
    df["macd_signal"] = macd.macd_signal()
    df["macd_hist"] = macd.macd_diff()

    # ==========================
    # ADX
    # ==========================

    adx = ADXIndicator(
        high=high,
        low=low,
        close=close
    )

    df["adx"] = adx.adx()

    # ==========================
    # Bollinger Bands
    # ==========================

    bb = BollingerBands(close=close)

    df["bb_upper"] = bb.bollinger_hband()
    df["bb_middle"] = bb.bollinger_mavg()
    df["bb_lower"] = bb.bollinger_lband()

    # ==========================
    # ATR
    # ==========================

    atr = AverageTrueRange(
        high=high,
        low=low,
        close=close
    )

    df["atr"] = atr.average_true_range()

    # ==========================
    # Candle calculations
    # ==========================

    df["body"] = (close - open_price).abs()

    df["upper_wick"] = high - close.where(close > open_price, open_price)

    df["lower_wick"] = close.where(close < open_price, open_price) - low

    # ==========================
    # Trend
    # ==========================

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