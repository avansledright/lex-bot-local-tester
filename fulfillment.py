import json
from datetime import datetime

def lambda_handler(event, context):
    print("Inside fulfillment")
    print(event)
    if event['currentIntent'] == "time":
        now = datetime.now()
        return now.strftime("%Y-%m-%d %H:%M")