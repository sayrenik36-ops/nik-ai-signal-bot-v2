from services.market_data import get_market_data
from strategies.indicators import calculate_indicators

print("=" * 60)
print("TESTING INDICATORS")
print("=" * 60)

df = get_market_data("EUR/USD")

if df is None:
    print("Failed to get market data.")
    exit()

df = calculate_indicators(df)

print(df.tail())

print("\nLATEST VALUES\n")

latest = df.iloc[-1]

print("Close   :", latest["close"])
print("EMA9    :", latest["ema9"])
print("EMA21   :", latest["ema21"])
print("EMA50   :", latest["ema50"])
print("EMA200  :", latest["ema200"])
print("RSI     :", latest["rsi"])
print("MACD    :", latest["macd"])
print("ADX     :", latest["adx"])
print("ATR     :", latest["atr"])
print("Trend   :", latest["trend"])
