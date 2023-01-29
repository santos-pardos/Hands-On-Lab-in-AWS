import requests
import boto3
import uuid
import time
import json

client = boto3.client('kinesis', region_name='us-east-1')
partition_key = str(uuid.uuid4())


def send_data_record(crypto="BTC"):
    base_url = "https://min-api.cryptocompare.com/data"
    r = requests.get(f"{base_url}/price?fsym={crypto}&tsyms=USD")
    data = r.json()
    data["timestamp"] = int(time.time())
    data["crypto"] = crypto
    result = client.put_record(StreamName="demo-kds",
                               Data=json.dumps(data),
                               PartitionKey=crypto)
    print(result)


while True:
    send_data_record("BTC")
    send_data_record("ETH")
    time.sleep(10)
