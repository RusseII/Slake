import boto3
from decimal import Decimal
import json
import uuid
import os
from telegram_bot import send_telegram_message, Status
from webhooks import send_webhooks
from dwelo import handle_dwelo
import asyncio


dynamodb = boto3.resource('dynamodb')

TABLE_NAME = os.environ['TABLE_NAME']


async def dynamodb_insert(payload):
    payload['id'] = str(uuid.uuid4())
    payload['clickType'] = payload['devicePayload']['clickType']
    payload['reportedTime'] = payload['devicePayload']['reportedTime']
    table = dynamodb.Table(TABLE_NAME)
    return table.put_item(
        Item=payload)
async def main(event, context):
    print(event)
    event = json.loads(json.dumps(event), parse_float=Decimal)


    webhook_data = {}
    webhook_data['user'] = event['placementInfo']['attributes'].get('user')
    webhook_data['status'] = Status[event['devicePayload']['clickType']].value

    L = await asyncio.gather(
        handle_dwelo(Status[event['devicePayload']['clickType']]),
        send_telegram_message(Status[event['devicePayload']['clickType']]),
        send_webhooks(webhook_data),
        dynamodb_insert(event)
    )

    print(L)
    return L


def handler(event, context):
    return asyncio.run(main(event, context))


test = {
  "deviceInfo": {
    "deviceId": "P5SJVQ2007V8296A",
    "type": "button",
    "remainingLife": 100,
    "attributes": {
      "projectRegion": "us-west-2",
      "projectName": "smart_home",
      "placementName": "test",
      "deviceTemplateName": "store-click"
    }
  },
  "deviceEvent": {
    "buttonClicked": {
      "clickType": "SINGLE",
      "reportedTime": "2021-06-24T10:38:56.735Z",
      "additionalInfo": {
        "version": "1.8.0"
      }
    }
  },
  "placementInfo": {
    "projectName": "smart_home",
    "placementName": "test",
    "attributes": {
      "user": "russell"
    },
    "devices": {
      "store-click": "P5SJVQ2007V8296A"
    }
  },
  "devicePayload": {
    "clickType": "SINGLE",
    "serialNumber": "P5SJVQ2007V8296A",
    "remainingLife": 100,
    "version": "1.8.0",
    "certificateId": "14b54e9fc9a8646e4517498102c3dad0e5d5333ba0e3b5ba17fc5321fc44ff35",
    "reportedTime": 1624531136735,
    "topic": "/Devices/Button/P5SJVQ"
  }
}
if __name__ == "__main__":
    
    handler(test, None)