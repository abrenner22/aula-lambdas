import json

def hello_world(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Hello, World!'})
    }
