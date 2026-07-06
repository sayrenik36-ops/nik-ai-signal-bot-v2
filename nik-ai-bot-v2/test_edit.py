from services.telegram_bot import send_signal, edit_message
import time

message_id = send_signal(
    pair="EUR/USD",
    signal="CALL",
    price=1.14520,
    score=88,
    reasons=[
        "EMA Bullish",
        "MACD Bullish",
        "Strong Up Trend"
    ]
)

print("Message ID:", message_id)

if message_id:
    time.sleep(5)

    new_message = """
<b>🚀 NIKHIL AI FOREX BOT V2.0</b>

<b>📊 SIGNAL RESULT</b>

━━━━━━━━━━━━━━━━━━

📈 Pair : EUR/USD

🟢 Signal : CALL

🏆 Result : ✅ WIN

━━━━━━━━━━━━━━━━━━

Today's Accuracy : 80%

Overall Accuracy : 84%
"""

    edit_message(message_id, new_message)
else:
    print("Failed to send Telegram message.")
