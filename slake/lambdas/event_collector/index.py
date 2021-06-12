import boto3
from decimal import Decimal
import json
import uuid
import os

dynamodb = boto3.resource('dynamodb')

TABLE_NAME = os.environ['TABLE_NAME']

def handler(event, context):
    print(event)
    event = json.loads(json.dumps(event), parse_float=Decimal)
    table = dynamodb.Table(TABLE_NAME)
    event['id'] = str(uuid.uuid4())
    event['clickType'] = event['devicePayload']['clickType']
    event['reportedTime'] = event['devicePayload']['reportedTime']

    response = table.put_item(
        Item=event
    )

    return response