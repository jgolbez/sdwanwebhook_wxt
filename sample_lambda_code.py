import json
#from botocore.vendored import requests
import urllib3
http = urllib3.PoolManager()
import os
token = os.environ['bearerToken']
roomid = os.environ['roomId']


headers={
'content-type': "application/json; charset=utf-8",
'authorization':"Bearer "+token,
'accept':"application/json"
}
url="https://webexapis.com/v1/messages"


def lambda_handler(event, context):
    print("POST Was Successful, proceeding to send alert")
    print(event['body'])
    print(json.loads(event['body']))
    data_dict = json.loads(event['body'])
    formatted_message = f"vManage Alert:\nComponent: {data_dict.get('component')}\nSeverity: {data_dict.get('severity')}\nSev#: {data_dict.get('severity_number')}\nHostname: {data_dict['values'][0]['host-name']}\nSystem-IP: {data_dict['values'][0]['system-ip']}\nError: {data_dict['values'][0]['status']}\nError Detail: {data_dict['values'][0]['type']}"
#    message = "```\n" + json.dumps(data_dict, sort_keys=True, indent=4) + "\n ```"
#    print(message)
    payload={
        "roomId": roomid,
        "markdown": formatted_message
        }
    response = http.request("POST", url, body=json.dumps(payload), headers=headers)
    print(response)
    print("Here's the message status:")
    print(response.status)
    
    
