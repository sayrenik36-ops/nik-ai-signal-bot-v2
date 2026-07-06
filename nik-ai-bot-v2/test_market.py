from services.market_data import get_market_data

print("=" * 60)
print("Testing TwelveData Connection")
print("=" * 60)

df = get_market_data("EUR/USD")

if df is None:
    print("❌ FAILED: No market data received.")
else:
    print("✅ SUCCESS: Market data received.")
    print()
    print(df.tail())
