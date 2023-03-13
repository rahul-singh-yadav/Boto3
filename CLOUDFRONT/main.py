import boto3
import os
import dotenv
from datetime import datetime

# Load environment variables from .env
dotenv.load_dotenv()

# Fetch current datetime.
current = datetime.now()

# Use client()
client = boto3.client('cloudfront')

# Fetch DistributionId from environment variables.
id = os.environ.get('CLOUDFRONT_ID')

# Fetch invalidation path from environemnt variables.
path = os.environ.get('INVALIDATION_PATH')

# Save responses
try:
    response_dict = client.create_invalidation(
    DistributionId = id,
        InvalidationBatch = {
            'Paths': {
                'Quantity': 1, 
                'Items': [str(path)]
            },
            'CallerReference': str(current)
        }
    )

    # Output response from cloudfront
    print(response_dict)

    # Get current working directory
    pwd = os.getcwd()

    # Filepath to which data would be written.
    file_path = os.path.join(pwd, 'responses.txt')

    # Save 'response' to a file, if the file doesn't exist, it creates it, appends data to it for future use.
    with open(file_path, 'a') as file:
        data = file.write(str(response_dict) + '\n')
        # file.close()
        
except client.exceptions.InvalidationBatchAlreadyExists as e:
    # Throws exception error message at stdout
    print(f"Invalidation requested already exist, try a unique caller reference: {e}")