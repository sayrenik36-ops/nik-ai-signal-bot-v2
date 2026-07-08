from services.telegram_service import send_message
from services.market_data import get_candles
from strategies.binary_ai import generate_signal


def create_signal():

    pair = "EUR/USD"

    candles = get_candles(
        pair,
        "1min",
        100
    )

    if candles is None:
        print("No candle data")
        return


    signal = generate_signal(candles)

    direction = signal["direction"]
    confidence = signal["confidence"]
    reason = signal["reason"]


    if confidence >= 85:

        emoji = "🟢" if direction == "CALL" else "🔴"

        message = f"""
🔥 <b>NIK AI LIVE SIGNAL</b>

Pair:
{pair}

Direction:
{direction} {emoji}

Expiry:
2 Minutes

Strategy:
EMA + RSI

Confidence:
{confidence}%

Reason:
{reason}
"""

        send_message(message)


    else:

        print(
            f"Signal ignored. Confidence only {confidence}%"
        )


if __name__ == "__main__":
    create_signal()
