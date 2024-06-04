import json
import boto3
import os

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = os.getenv('BUCKET_NAME')
    object_name = event['queryStringParameters']['object_name']
    
    try:
        presigned_url = s3.generate_presigned_url('put_object', 
                                                  Params={'Bucket': bucket_name, 'Key': object_name}, 
                                                  ExpiresIn=3600,
                                                  HttpMethod='PUT')
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps('Error generating presigned URL: {}'.format(str(e)))
        }
    
    return {
        'statusCode': 200,
        'body': json.dumps({'url': presigned_url})
    }
