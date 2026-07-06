from services.market_data import get_market_data

df = get_market_data("EUR/USD")

if df is not None:
    print(df.tail())
else:
    print("No data received.")