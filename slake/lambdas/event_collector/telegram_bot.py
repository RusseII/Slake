from enum import Enum
from secrets import get_secret
import aiohttp
import random


morning_messages = ["@sven Do u want to actually be kind? Use https://80000hours.org/ or come to the conclusions yourself of how you can make a positive impact.", "@petioo @sven @gatesyp good morning. Don't forget to schedule your focusmates for today!", "@petioo @sven @gatesyp good morning let's start out our day with a 5 min braindump exersise https://www.squibler.io/dangerous-writing-prompt-app/write?limit=5&type=minutes :)", "@petioo @sven @gatesyp don't forget that i'm always here for you !!  Good morning =]",
                    "Monday inspiration to start the day. Is it monday ...? WHo knows .... RANT TIME everyday should be monday !!! DO WHAT u love if ur not enjoying ur life start making changes TODAY to improve it! ", "You make the culture. The things you do today set the culture for others tomorrow. Live your live in a way that inspires others. https://en.wikipedia.org/wiki/Status_quo_bias", "Is your enviroment set up in a way that it promotes your good habbits and detracts from your bad? https://jamesclear.com/choice-architecture"]


night_messages = ["Good night sleep well.", "@petipoo i'm heading off to sleep hope you join me soon!", "@gatesyp NIGHTY NIGHT don't come in!!!!!!", "@sven going to sleep hope to see u in the morning! flights.russell.work ", "Bed time. ", "Beep Boop Russell just clicked me and appears to be going to sleep.", "Beep Boop - Russell if it's past 10pm EST your going to get PUNISHED!", "Beep Boop Goodnight Russsell :) ", "Beep Boop I'll keep the house nice and cool while you sleep goodnight Russell :) ", "Peti you make a good friend goodnight", "@gatesyp thank for getting me involved in hackathons in college goodnight :) ",
                  "@petioo I hope your knee is healing well I'm looking forward to scooting in my dreams! NIGHTY! ", "@gatesyp Will be dreaming of our future trips together like Okinawa :) NIGHTY! ", "@gatesyp Goodnight let's work to be our best. That starts tonight ...", "@petioo Goodnight DR PETE can u please give me a perscription for a good nights sleep? ", "@petioo Lets enjoy our good nights sleep while we can. Once in NYC there will be 247 honking and no sleep. ", "@petioo Hope the cats cuddle you to sleep tonight! ", "@sven WIll be dreaming of the future pizzas we eat. ", "@sven Sleeping my way one day closer to tomorrowland ", "@sven Poland Japan Spain Mexico ... tahts it? will be drameing of new countries "]
chat_id = -475570287


class Status(Enum):
    SINGLE = "awake"
    DOUBLE = "asleep"


async def send_telegram_message(status: Status):
    print(f'started {send_telegram_message.__name__}')
    if (status == Status.SINGLE):
        return await send(random_morning_message())

    if (status == Status.DOUBLE):
        return await send(random_night_message())


def random_morning_message():
    return random.choice(morning_messages)


def random_night_message():
    return random.choice(night_messages)


async def send(message: str):
    RUSSELL_BOT_API_KEY = get_secret(
        "russell_bot_api_key", "RUSSELL_BOT_API_KEY")
    async with aiohttp.ClientSession() as session:
        payload = {"chat_id": chat_id, "text": message}
        async with session.post(f'https://api.telegram.org/bot{RUSSELL_BOT_API_KEY}/sendMessage',
                                json=payload) as resp:
            return resp.status


if __name__ == "__main__":
    print(random_night_message())
    print(random_morning_message())