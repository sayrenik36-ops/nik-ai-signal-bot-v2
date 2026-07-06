"""
=========================================================
NIKHIL AI FOREX BOT V2.0
AI Strategy Engine
=========================================================
"""

from config import MIN_AI_SCORE


def get_signal(df):

    latest = df.iloc[-1]

    score = 0

    reasons = []

    buy = 0

    sell = 0

    # ==========================
    # EMA Trend
    # ==========================

    if latest["ema9"] > latest["ema21"] > latest["ema50"]:

        buy += 25
        reasons.append("EMA Bullish")

    elif latest["ema9"] < latest["ema21"] < latest["ema50"]:

        sell += 25
        reasons.append("EMA Bearish")

    # ==========================
    # RSI
    # ==========================

    if latest["rsi"] < 30:

        buy += 20
        reasons.append("RSI Oversold")

    elif latest["rsi"] > 70:

        sell += 20
        reasons.append("RSI Overbought")

    # ==========================
    # MACD
    # ==========================

    if latest["macd"] > latest["macd_signal"]:

        buy += 20
        reasons.append("MACD Bullish")

    else:

        sell += 20
        reasons.append("MACD Bearish")

    # ==========================
    # ADX
    # ==========================

    if latest["adx"] > 25:

        if buy > sell:

            buy += 15
            reasons.append("Strong Up Trend")

        elif sell > buy:

            sell += 15
            reasons.append("Strong Down Trend")

    # ==========================
    # Bollinger Bands
    # ==========================

    if latest["close"] <= latest["bb_lower"]:

        buy += 10
        reasons.append("Lower Bollinger")

    elif latest["close"] >= latest["bb_upper"]:

        sell += 10
        reasons.append("Upper Bollinger")

    # ==========================
    # Final Decision
    # ==========================

    if buy > sell:

        signal = "CALL"
        score = buy

    elif sell > buy:

        signal = "PUT"
        score = sell

    else:

        signal = "WAIT"
        score = 0

    if score < MIN_AI_SCORE:

        signal = "WAIT"

    return signal, score, reasons
