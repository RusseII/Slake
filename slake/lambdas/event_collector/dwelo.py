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



def lock_devices(auth_token):
    lockId = "381219"
    lock_command = {"command":"lock"}
    print(auth_token)
    headers={"authorization": auth_token}
    resp = requests.post(f'{dwelo_url}/device/{lockId}/command', json=lock_command, headers=headers)
    print(resp.json())


def turn_off_lights(auth_token):
    lockId = "381217"
    lock_command = {"command":"off"}
    headers={"authorization": auth_token}
    resp = requests.post(f'{dwelo_url}/device/{lockId}/command', json=lock_command, headers=headers)
    print(resp.json())


def handle_dwelo():
    token = get_auth_token()
    lock_devices(token)
    turn_off_lights(token)

if __name__ == "__main__":
    handle_dwelo()