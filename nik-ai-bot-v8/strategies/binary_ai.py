from strategies.indicators import analyze


def generate_signal(df):

    result = analyze(df)

    ema_signal = result["ema_signal"]
    rsi = result["rsi"]

    confidence = 50
    reasons = []

    direction = None


    if rsi is None:
        return {
            "direction": None,
            "confidence": 0,
            "reason": "RSI unavailable"
        }


    # EMA trend
    if ema_signal == "BUY":
        confidence += 20
        reasons.append("EMA bullish")
    else:
        confidence += 20
        reasons.append("EMA bearish")


    # RSI logic
    if rsi < 30:

        direction = "CALL"
        confidence += 30
        reasons.append(
            f"RSI oversold {round(rsi,2)}"
        )


    elif rsi > 70:

        direction = "PUT"
        confidence += 30
        reasons.append(
            f"RSI overbought {round(rsi,2)}"
        )


    elif rsi < 45:

        direction = "CALL"
        confidence += 10
        reasons.append(
            f"RSI weak {round(rsi,2)}"
        )


    elif rsi > 55:

        direction = "PUT"
        confidence += 10
        reasons.append(
            f"RSI strong {round(rsi,2)}"
        )


    else:

        return {
            "direction": None,
            "confidence": 40,
            "reason": f"RSI neutral {round(rsi,2)}"
        }


    return {
        "direction": direction,
        "confidence": min(confidence,95),
        "reason": ", ".join(reasons)
    }
