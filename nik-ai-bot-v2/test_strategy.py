from services.market_data import get_market_data
from strategies.indicators import calculate_indicators
from strategies.strategy import get_signal

print("=" * 60)
print("TESTING AI STRATEGY")
print("=" * 60)

df = get_market_data("EUR/USD")

if df is None:
    print("Market Data Failed")
    exit()

df = calculate_indicators(df)

signal, score, reasons = get_signal(df)

print()

print("Signal :", signal)
print("Score  :", score)

print()

print("Reasons")

for reason in reasons:
    print("-", reason)
