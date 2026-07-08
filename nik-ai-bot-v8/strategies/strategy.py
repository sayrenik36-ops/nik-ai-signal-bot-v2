"""
=========================================================
NIK AI BINARY BOT V8
Professional Strategy Engine
=========================================================
"""


class Strategy:

    @staticmethod
    def analyse(df):

        last = df.iloc[-1]

        buy = 0
        sell = 0

        reasons_buy = []
        reasons_sell = []

        # =====================================
        # EMA TREND
        # =====================================

        if last["ema20"] > last["ema50"] > last["ema200"]:
            buy += 20
            reasons_buy.append("EMA Trend")

        elif last["ema20"] < last["ema50"] < last["ema200"]:
            sell += 20
            reasons_sell.append("EMA Trend")

        # =====================================
        # RSI
        # =====================================

        if last["rsi"] < 30:
            buy += 15
            reasons_buy.append("RSI Oversold")

        elif last["rsi"] > 70:
            sell += 15
            reasons_sell.append("RSI Overbought")

        # =====================================
        # MACD
        # =====================================

        if last["macd"] > last["macd_signal"]:
            buy += 15
            reasons_buy.append("MACD Bullish")

        else:
            sell += 15
            reasons_sell.append("MACD Bearish")

        # =====================================
        # SUPERTREND
        # =====================================

        if last["close"] > last["supertrend"]:
            buy += 15
            reasons_buy.append("SuperTrend")

        else:
            sell += 15
            reasons_sell.append("SuperTrend")

        # =====================================
        # ADX
        # =====================================

        if last["adx"] > 25:

            if buy > sell:
                buy += 10
                reasons_buy.append("Strong Trend")

            else:
                sell += 10
                reasons_sell.append("Strong Trend")

        # =====================================
        # BOLLINGER
        # =====================================

        if last["close"] <= last["bb_lower"]:
            buy += 10
            reasons_buy.append("BB Lower")

        elif last["close"] >= last["bb_upper"]:
            sell += 10
            reasons_sell.append("BB Upper")

        # =====================================
        # ENGULFING
        # =====================================

        if last["bullish_engulfing"]:
            buy += 10
            reasons_buy.append("Bullish Engulfing")

        if last["bearish_engulfing"]:
            sell += 10
            reasons_sell.append("Bearish Engulfing")

        # =====================================
        # PIN BAR
        # =====================================

        if last["pinbar_buy"]:
            buy += 5
            reasons_buy.append("Pin Bar")

        if last["pinbar_sell"]:
            sell += 5
            reasons_sell.append("Pin Bar")

        # =====================================
        # DOJI
        # =====================================

        if last["doji"]:
            buy -= 5
            sell -= 5

        # =====================================
        # MOMENTUM
        # =====================================

        if last["momentum"] > 0:
            buy += 10
            reasons_buy.append("Momentum")

        elif last["momentum"] < 0:
            sell += 10
            reasons_sell.append("Momentum")

        # =====================================
        # VWAP
        # =====================================

        if last["close"] > last["vwap"]:
            buy += 10
            reasons_buy.append("VWAP")

        else:
            sell += 10
            reasons_sell.append("VWAP")

        # =====================================
        # FINAL RESULT
        # =====================================

        confidence = max(buy, sell)

        if buy > sell:

            signal = "CALL"

        elif sell > buy:

            signal = "PUT"

        else:

            signal = "NO TRADE"

        return {

            "signal": signal,

            "confidence": confidence,

            "buy_score": buy,

            "sell_score": sell,

            "buy_reasons": reasons_buy,

            "sell_reasons": reasons_sell,

        }