import pandas as pd


def calculate_ema(data, period):

    return data["close"].ewm(
        span=period,
        adjust=False
    ).mean()



def calculate_rsi(data, period=14):

    delta = data["close"].diff()

    gain = delta.clip(lower=0)

    loss = -delta.clip(upper=0)


    avg_gain = gain.rolling(period).mean()

    avg_loss = loss.rolling(period).mean()


    rs = avg_gain / avg_loss


    return 100 - (100/(1+rs))



def analyze(data):

    data["EMA9"] = calculate_ema(
        data,
        9
    )

    data["EMA21"] = calculate_ema(
        data,
        21
    )

    data["RSI"] = calculate_rsi(
        data
    )


    latest = data.iloc[-1]


    return {

        "ema_signal":
            "BUY"
            if latest.EMA9 > latest.EMA21
            else "SELL",


        "rsi":
            round(
                float(latest.RSI),
                2
            )
            if not pd.isna(latest.RSI)
            else None
    }
