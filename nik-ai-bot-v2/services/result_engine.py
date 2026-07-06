import time
from services.telegram_bot import edit_message
from database import db
from services.market_data import get_market_data


def calculate_result(entry, exit_price, signal):

    if signal == "CALL":

        if exit_price > entry:
            return "WIN"
        else:
            return "LOSS"

    if signal == "PUT":

        if exit_price < entry:
            return "WIN"
        else:
            return "LOSS"

    return "DRAW"


def run_result_engine(pair, entry_price, signal, message_id, signal_id):

    print(f"⏳ Waiting for expiry: {pair}")

    # WAIT 60 seconds (expiry time)
    time.sleep(60)

    # GET new price
    df = get_market_data(pair)

    if df is None or df.empty:
        print("❌ No exit data")
        return

    exit_price = df.iloc[-1]["close"]

    # CALCULATE RESULT
    result = calculate_result(entry_price, exit_price, signal)

    # UPDATE DATABASE
    db.update_result(
        signal_id,
        exit_price,
        result
    )

    # BUILD TELEGRAM RESULT MESSAGE
    emoji = "🏆" if result == "WIN" else "❌"

    message = f"""
<b>🏆 RESULT</b>

📈 Pair : {pair}

{emoji} Signal : {signal}

📊 Result : {result}

💰 Entry : {entry_price}
💰 Exit : {exit_price}
"""

    # EDIT ORIGINAL MESSAGE
    edit_message(message_id, message)

    print(f"✅ Result Updated: {result}")
