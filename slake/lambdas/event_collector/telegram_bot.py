import requests
from enum import Enum
from secrets import get_secret


chat_id = -475570287


class Status(Enum):
    SINGLE = "awake"
    DOUBLE = "asleep"


def send_telegram_message(status: Status):
    if (status == Status.SINGLE):
        send("Hello good morning :) Looking forward to a great day!")

    if (status == Status.DOUBLE):
        send('Time to turn off electronics 4 bed. Cant wait until tomorrow!')


def send(message: str):
    RUSSELL_BOT_API_KEY = get_secret(
        "russell_bot_api_key", "RUSSELL_BOT_API_KEY")
    requests.post(f'https://api.telegram.org/bot{RUSSELL_BOT_API_KEY}/sendMessage', data={
        "chat_id": chat_id, "text": message})
