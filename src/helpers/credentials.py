import os
import boto3

class credential_helper:
    @staticmethod
    def create_new_session():
        return boto3.Session(
        aws_access_key_id = os.environ.get('AWS_CLIENT_ID'),
        aws_secret_access_key = os.environ.get('AWS_CLIENT_SECRET'),
      	region_name = os.environ.get('AWS_REGION', 'us-west-2')
    )