from enum import Enum
from secrets import get_secret
import aiohttp


chat_id = -475570287


class Status(Enum):
    SINGLE = "awake"
    DOUBLE = "asleep"


async def send_telegram_message(status: Status):
    print(f'started {send_telegram_message.__name__}')
    if (status == Status.SINGLE):
        return await send("Hello good morning :) Looking forward to a great day!")

    if (status == Status.DOUBLE):
       return await send('Time to turn off electronics 4 bed. Cant wait until tomorrow!')


async def send(message: str):
    RUSSELL_BOT_API_KEY = get_secret(
        "russell_bot_api_key", "RUSSELL_BOT_API_KEY")
    async with aiohttp.ClientSession() as session:
        payload = {"chat_id": chat_id, "text": message}
        async with session.post(f'https://api.telegram.org/bot{RUSSELL_BOT_API_KEY}/sendMessage',
                                json=payload) as resp:
            return await resp.json()

