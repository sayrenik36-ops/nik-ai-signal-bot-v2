from services.telegram_bot import send_signal

send_signal(
    pair="EUR/USD",
    signal="CALL",
    price=1.14235,
    score=82,
    reasons=[
        "EMA Bullish",
        "MACD Bullish",
        "ADX Strong Trend",
        "RSI Support"
    ]
)
