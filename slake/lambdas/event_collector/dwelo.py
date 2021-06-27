from secrets import get_secret
import requests
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

    def off(self):
        resp = requests.post(
            f'{dwelo_url}/device/{self.device.id}/command', json=self.device.command, headers=self.headers)
        print(resp.json())


class Light:
    id = "381217"
    command = {"command": "off"}


class Lock:
    id = "381219"
    command = {"command": "lock"}


def handle_dwelo():
    token = get_auth_token()
    kitchen_light = Dwelo_Device(Light(), token)
    lock = Dwelo_Device(Lock(), token)
    kitchen_light.off()
    lock.off()



if __name__ == "__main__":
    handle_dwelo()
