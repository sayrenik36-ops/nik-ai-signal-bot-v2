import requests
from config import BOT_TOKEN, CHAT_ID

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

response = requests.post(
    url,
    data={
        "chat_id": CHAT_ID,
        "text": "✅ NIK AI BOT TEST MESSAGE\nTelegram connection successful!"
    }
)

print("Status Code:", response.status_code)
print(response.text)