from services.signal_manager import process_signal

print("=" * 60)
print("TESTING SIGNAL MANAGER")
print("=" * 60)

process_signal(
    pair="EUR/USD",
    signal="CALL",
    price=1.14050,
    score=85,
    reasons=[
        "EMA Bullish",
        "MACD Bullish",
        "Strong Trend"
    ]
)
