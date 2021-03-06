import aiohttp
from telegram_bot import Status
from dataclasses import dataclass
from secrets import get_secret
import requests
import asyncio

dwelo_url = 'https://api.dwelo.com/v3'


def get_auth_token():
    password = get_secret('RUSSELL_DWELO_PASS', 'RUSSELL_DWELO_PASS')
    login_credentials = {"email": "rratcliffe57@gmail.com",
                         "password": password, "applicationId": "concierge"}
    auth_data = requests.post(dwelo_url + '/login/', json=login_credentials)
    auth_token = auth_data.json()['token']
    return auth_token


class Dwelo_Device:
    def __init__(self, device, auth_token):
        self.device = device
        self.headers = {"authorization": auth_token}

    async def off(self):
        async with aiohttp.ClientSession() as session:
            async with session.post(
                    f'{dwelo_url}/device/{self.device.id}/command', json=self.device.off_command, headers=self.headers) as resp:
                print(await resp.json())
                return resp.status

    async def on(self):
        async with aiohttp.ClientSession() as session:
            async with session.post(
                    f'{dwelo_url}/device/{self.device.id}/command', json=self.device.on_command, headers=self.headers) as resp:
                print(await resp.json())
                return resp.status


@dataclass(frozen=True)
class Light:
    id = "381217"
    on_command = {"command": "on"}
    off_command = {"command": "off"}


@dataclass(frozen=True)
class Lock:
    id = "381219"
    on_command = {"command": "lock"}
    off_command = {"command": "unlock"}


async def handle_dwelo(status: Status):
    print(f'started {handle_dwelo.__name__}')
    token = get_auth_token()
    kitchen_light = Dwelo_Device(Light(), token)
    lock = Dwelo_Device(Lock(), token)
    if (status == Status.SINGLE):
        return await asyncio.gather(
            kitchen_light.on(),
            lock.off())

    if (status == Status.DOUBLE):
        return await asyncio.gather(
            kitchen_light.off(),
            lock.on())


if __name__ == "__main__":
    handle_dwelo()
