from services.market_data import market

print("=" * 60)
print("NIK AI MARKET DATA TEST")
print("=" * 60)

df = market.get_market_data(
    "EUR/USD",
    interval="1min"
)

if df is None:

    print("No Market Data")

else:

    print(df.tail())

    print()

    print("Live Price")

    print(market.get_live_price("EUR/USD"))
