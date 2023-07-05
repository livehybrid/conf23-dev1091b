import boto3
import json
import datetime


def lambda_handler(event, context):

    now = datetime.datetime.now()
    midnight = datetime.datetime.combine(now.date(), datetime.time())
    tenSecondBlocks = int((now - midnight).seconds/10)
    lineNumbers = [tenSecondBlocks-6+i for i in range(1,7)]
    readingFile=open('data.json')
    readingLines=readingFile.readlines()

    newReadings = []
    count = 0
    for reading in [json.loads(readingLines[n]) for n in lineNumbers]:
        from pprint import pprint
        reading['readAt'] = (midnight + (datetime.timedelta(seconds=lineNumbers[count]*10))).strftime("%Y-%m-%dT%H:%M:%S+00:00")
        newReadings.append(reading)
        count = count + 1
    
    if (event['httpMethod']!="GET"):
        return {
            'statusCode': '400' ,
            'body': json.dumps({"error":"Please use GET method only"}),
            'headers': {
                'Content-Type': 'application/json',
            }
        }
    else:
        return {
            'statusCode': '200',
            'body': json.dumps(newReadings),
            'headers': {
                'Content-Type': 'application/json',
            },
        }
    
