from services.market_data import market

df = market.get_market_data(
    "EUR/USD",
    "1min",
)

print(df.tail())

print()

print("Live Price")

print(market.get_live_price("EUR/USD"))