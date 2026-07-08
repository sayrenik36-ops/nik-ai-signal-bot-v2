import requests
from config import BOT_TOKEN

url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"

r = requests.get(url)

print(r.status_code)
print(r.text)
