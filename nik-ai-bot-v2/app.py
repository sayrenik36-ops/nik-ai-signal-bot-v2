"""
=========================================================
NIKHIL AI FOREX BOT V2.0
Main Application
=========================================================
"""

import time

from config import (
    PAIRS,
    SCAN_INTERVAL,
)

from services.market_data import get_market_data
from strategies.indicators import calculate_indicators
from strategies.strategy import get_signal
from services.signal_manager import process_signal


def print_header():

    print("\n" + "=" * 70)
    print("🚀 NIKHIL AI FOREX BOT V2.0")
    print("=" * 70)


def scan_pair(pair_name, symbol):

    print(f"\nScanning : {pair_name}")

    df = get_market_data(symbol)

    if df is None:

        print("Market data unavailable.")

        return

    df = calculate_indicators(df)

    signal, score, reasons = get_signal(df)

    latest = df.iloc[-1]

    price = float(latest["close"])

    print(f"Price     : {price:.5f}")
    print(f"Signal    : {signal}")
    print(f"AI Score  : {score}")

    if reasons:

        print("Reasons")

        for reason in reasons:

            print(f"  • {reason}")

    process_signal(

        pair=pair_name,

        signal=signal,

        price=price,

        score=score,

        reasons=reasons

    )


def main():

    print_header()

    print("Bot Started Successfully")

    while True:

        print("\n" + "=" * 70)
        print("Starting New Scan")
        print("=" * 70)

        for pair_name, symbol in PAIRS.items():

            try:

                scan_pair(pair_name, symbol)

            except Exception as e:

                print(f"\nERROR while scanning {pair_name}")
                print(e)

        print("\nScan Completed")
        print(f"Waiting {SCAN_INTERVAL} seconds...")

        time.sleep(SCAN_INTERVAL)


if __name__ == "__main__":

    main()