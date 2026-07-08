import requests
from config import BOT_TOKEN, CHAT_ID


def send_message(message):

    url = (
        f"https://api.telegram.org/bot{BOT_TOKEN}"
        "/sendMessage"
    )

    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    }

    try:
        response = requests.post(
            url,
            json=payload,
            timeout=10
        )

        print(response.text)

        return True

    except Exception as e:
        print("Telegram error:", e)
        return False
