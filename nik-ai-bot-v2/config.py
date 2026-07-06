"""
=========================================================
NIKHIL AI FOREX BOT V2.0
Configuration
=========================================================
"""

import os

# =====================================================
# API SETTINGS
# =====================================================

# Get these from environment variables.
# During development you can replace them with your own keys if needed.
API_KEY = os.getenv("TWELVEDATA_API_KEY", "")

# =====================================================
# TELEGRAM
# =====================================================

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")

CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")

# =====================================================
# MARKET SETTINGS
# =====================================================

TIMEFRAME = "1min"

OUTPUT_SIZE = 200

SCAN_INTERVAL = 60

EXPIRY_MINUTES = 1

# =====================================================
# AI SETTINGS
# =====================================================

MIN_AI_SCORE = 40

# Indicator switches

USE_EMA = True
USE_MACD = True
USE_RSI = True
USE_ADX = True
USE_BOLLINGER = True
USE_ATR = True

# =====================================================
# FOREX PAIRS
# =====================================================

PAIRS = {
    "EUR/USD": "EUR/USD",
    "GBP/USD": "GBP/USD",
    "USD/JPY": "USD/JPY",
    "AUD/USD": "AUD/USD",
    "USD/CAD": "USD/CAD",
    "USD/CHF": "USD/CHF",
    "NZD/USD": "NZD/USD"
}

# =====================================================
# DATABASE
# =====================================================

DATABASE_FOLDER = "database"

DATABASE_NAME = "signals.db"

DATABASE_PATH = os.path.join(
    DATABASE_FOLDER,
    DATABASE_NAME
)

# =====================================================
# LOGGING
# =====================================================

LOG_FOLDER = "logs"

LOG_FILE = os.path.join(
    LOG_FOLDER,
    "bot.log"
)

# =====================================================
# VERSION
# =====================================================

BOT_NAME = "NIKHIL AI FOREX BOT"

BOT_VERSION = "2.0.0"