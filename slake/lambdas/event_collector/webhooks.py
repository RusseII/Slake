import requests

webhookUrls = ["https://hooks.nabu.casa/gAAAAABgz6UJ3pIqj-Ijc9347eeeG2mUKRJbVkzViEdjsdOVde2VU1nYHjtL8xAQDmLtf6oUDzIgmKWjoeE6Y8uXtcO9Dpv954794oJeko-U0KqXLRTjrruq5Kk_gbDG9RRcxaJHaVRJwkE3jfm04UfIkzJyGoBpVfjJh7XSno3rGH-glLryO5M="]



def send_webhooks(data):
    for url in webhookUrls:
        requests.post(url, json=data)