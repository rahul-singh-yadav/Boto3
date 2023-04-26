import os
import boto3
import json
import boto3.session
import botocore.exceptions
from datetime import datetime

"""Retrieve configuration locations
    1. from .env file using dotenv.load_dotenv()

        # Load environment variables from .env
        # To do: throw exception if .env file doesn't exist in pwd.
    2. from aws configuration file at ~/.aws/conf using .Session()

        # Set session to use aws profile
        # session = boto3.session.Session(profile_name='<aws_profile>')
    3. injecting configuration directly in python script
"""

# Creates a low level client
ec2 = boto3.client('ec2')

# Uses collection to paginate through all available nodes
instances = ec2.describe_instances()['Reservations'][0]['Instances']

print(instances)

# Fetch all running nodes info. in current region
try:
    for i, instance in instances:
        print(f"\n Instance Id: \t ({instance['InstanceId']}, {instance['PublicIpAddress']})")

except botocore.exceptions.ClientError as e:
    print(f"An exception was raised with a message:\n {e}")
