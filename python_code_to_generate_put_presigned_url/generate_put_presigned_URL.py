import argparse
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def generate_presigned_url(bucket_name, object_key, expiration=3600):
    # Initialize the S3 client
    s3_client = boto3.client('s3')

    try:
        # Generate a presigned URL for the S3 object
        response = s3_client.generate_presigned_url('put_object',
                                                    Params={'Bucket': bucket_name,
                                                            'Key': object_key},
                                                    ExpiresIn=expiration)
    except (NoCredentialsError, PartialCredentialsError):
        print("Error: AWS credentials not found.")
        return None

    # The response contains the presigned URL
    return response

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Generate a presigned URL for uploading to S3.')
    parser.add_argument('bucket_name', type=str, help='The name of the S3 bucket.')
    parser.add_argument('object_key', type=str, help='The object key in the S3 bucket.')
    parser.add_argument('--expiration', type=int, default=3600, help='Time in seconds for the presigned URL to expire.')

    args = parser.parse_args()

    # Call the function with parsed arguments
    presigned_url = generate_presigned_url(args.bucket_name, args.object_key, args.expiration)
    
    # Check if the presigned URL was successfully generated
    if presigned_url:
        print(f'Presigned URL to upload file: {presigned_url}')
    else:
        print('Failed to generate presigned URL')
