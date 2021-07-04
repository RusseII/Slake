import aiohttp

webhookUrls = ["https://hooks.nabu.casa/gAAAAABgz6UJ3pIqj-Ijc9347eeeG2mUKRJbVkzViEdjsdOVde2VU1nYHjtL8xAQDmLtf6oUDzIgmKWjoeE6Y8uXtcO9Dpv954794oJeko-U0KqXLRTjrruq5Kk_gbDG9RRcxaJHaVRJwkE3jfm04UfIkzJyGoBpVfjJh7XSno3rGH-glLryO5M="]



async def send_webhooks(payload):
    print(f'started {send_webhooks.__name__}')
    responses = []
    for url in webhookUrls:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload ) as resp:
                print(f'webhook sent to ${url}')
                responses.append(resp.status)
    return responses