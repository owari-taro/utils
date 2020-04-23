import json
import urllib.parse
import boto3
from boto3.dynamodb.conditions import Key, Attr
TABLENAME = "mailaddress"
QUEUENAME = ""


def lambda_handler(event, context):
    dynamodb = boto3.resource("dynamodb")
    # TODO:using enviroment variable
    table = dynamodb.Table(TABLENAME)

    sqs = boto3.resource("sqs")
    queue = sqs.get_queue_by_name(QueueName=QUEUENAME)

    for rec in event["Records"]:
        backet_name = rec["s3"]["bucket"]["name"]
        filename = rec["s3"]["object"]["key"]
        #select records from dynamodb ,using secondary index
        response = table.query(IndexName="haserror-index",
                               KeyConditionExpression=Key("haserror").eq(0))

