import json
import pytz
from datetime import datetime
from pytz import timezone

def endpoint(event, context):
    current_time = datetime.datetime.now().time()
    body = {
        "message": "Hello, the time is " + str(current_time)
    }
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

def ist(event, context):
    IST = pytz.timezone('Asia/Kolkata')

    body = {
        "message": "Hello, Indian time is " + str(IST)
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    return response

def pst(event, context):
    PST = pytz.timezone('US/Pacific')

    # body = {
    #     "message": "Hello, US time is " + str(PST)
    # }

    response = {
        "statusCode": 200,
        "body": json.dumps({"message":str(PST)})
    }

    return response