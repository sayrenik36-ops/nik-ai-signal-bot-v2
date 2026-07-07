class Strategy:

    @staticmethod
    def analyse(df):

        last = df.iloc[-1]

        score_buy = 0
        score_sell = 0

        # EMA Trend
        if last["ema20"] > last["ema50"] > last["ema200"]:
            score_buy += 20

        if last["ema20"] < last["ema50"] < last["ema200"]:
            score_sell += 20

        # RSI
        if last["rsi"] < 35:
            score_buy += 20

        if last["rsi"] > 65:
            score_sell += 20

        # MACD
        if last["macd"] > last["macd_signal"]:
            score_buy += 20

        if last["macd"] < last["macd_signal"]:
            score_sell += 20

        # ADX
        if last["adx"] > 25:
            score_buy += 20
            score_sell += 20

        # Bollinger Bands
        if last["close"] < last["bb_lower"]:
            score_buy += 20

        if last["close"] > last["bb_upper"]:
            score_sell += 20

        if score_buy >= score_sell:
            signal = "BUY"
            score = score_buy
        else:
            signal = "SELL"
            score = score_sell

        return signal, score