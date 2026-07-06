"""
=========================================================
NIKHIL AI FOREX BOT V2.0
Telegram Service
=========================================================
"""
import requests

from datetime import datetime, timedelta

from zoneinfo import ZoneInfo

from config import BOT_TOKEN, CHAT_ID

BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"


# =========================================================
# Send Normal Message
# =========================================================

def send_message(message):

    url = f"{BASE_URL}/sendMessage"

    payload = {

        "chat_id": CHAT_ID,

        "text": message,

        "parse_mode": "HTML"

    }

    try:

        response = requests.post(
            url,
            data=payload,
            timeout=20
        )

        data = response.json()

        if data.get("ok"):

            print("✅ Telegram Message Sent")

            return data["result"]

        print("Telegram Error")

        print(data)

        return None

    except Exception as e:

        print("Telegram Exception")

        print(e)

        return None


# =========================================================
# Send Signal
# =========================================================

def send_signal(

    pair,

    signal,

    price,

    score,

    reasons

):

    emoji = "🟢"

    if signal == "PUT":
        emoji = "🔴"

    # Current Indian Time
    entry_time = datetime.now(
        ZoneInfo("Asia/Kolkata")
    )

    expiry_time = entry_time + timedelta(minutes=1)

    entry_time = entry_time.strftime("%H:%M:%p")

    expiry_time = expiry_time.strftime("%H:%M:%p")

    message = f"""
<b>🚀 NIKHIL AI FOREX BOT V2.0</b>

<b>📢 NEW SIGNAL</b>

━━━━━━━━━━━━━━━━━━

📈 <b>Pair :</b> {pair}

{emoji} <b>Signal :</b> {signal}

🕒 <b>Entry Time :</b> {entry_time} IST

⌛ <b>Expiry Time :</b> {expiry_time} IST

🧠 <b>AI Score :</b> {score}%

━━━━━━━━━━━━━━━━━━

<b>Reasons</b>

"""

    for reason in reasons:

        message += f"✅ {reason}\n"

    result = send_message(message)

    if result is None:

        return None

    return result["message_id"]
