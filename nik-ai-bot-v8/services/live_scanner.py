import time
from datetime import datetime, timedelta
import pytz

from services.market_data import get_candles
from strategies.binary_ai import generate_signal
from services.telegram_service import send_message


PAIRS = [
    "EUR/USD",
    "GBP/USD",
    "USD/JPY",
    "AUD/USD",
    "EUR/GBP"
]


MIN_CONFIDENCE = 80


def create_signal_message(pair, signal):

    india = pytz.timezone("Asia/Kolkata")

    now = datetime.now(india)

    # Entry after 1 minute
    entry_time = now + timedelta(minutes=1)

    entry_time = entry_time.replace(
        second=0,
        microsecond=0
    )

    direction = signal["direction"]

    if direction == "CALL":
        emoji = "🟢"
    else:
        emoji = "🔴"


    message = f"""
🔥 <b>NIK AI LIVE SIGNAL</b>

Pair:
{pair}

Direction:
{direction} {emoji}

Entry Time:
{entry_time.strftime('%H:%M')} IST

Expiry:
2 Minutes

Signal Sent:
{now.strftime('%H:%M')} IST

Strategy:
EMA + RSI

Confidence:
{signal['confidence']}%

Reason:
{signal['reason']}
"""

    return message



def scan_market():

    print("Scanning market...")


    for pair in PAIRS:

        try:

            candles = get_candles(
                symbol=pair
            )


            if candles is None:

                print(
                    pair,
                    "No data"
                )

                continue



            signal = generate_signal(
                candles
            )


            confidence = signal.get(
                "confidence",
                0
            )


            direction = signal.get(
                "direction"
            )


            if direction is None:

                print(
                    pair,
                    "ignored",
                    confidence
                )

                continue



            if confidence < MIN_CONFIDENCE:

                print(
                    pair,
                    "low confidence",
                    confidence
                )

                continue



            message = create_signal_message(
                pair,
                signal
            )


            send_message(
                message
            )


            print(
                "SIGNAL SENT:",
                pair,
                signal
            )



        except Exception as e:

            print(
                pair,
                "ERROR",
                e
            )



if __name__ == "__main__":


    while True:

        scan_market()

        time.sleep(60)
