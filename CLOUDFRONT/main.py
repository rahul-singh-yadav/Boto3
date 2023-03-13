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
    response = client.create_invalidation(
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
    print(response)

except client.exceptions.InvalidationBatchAlreadyExists as e:
    # Throws exception error message at stdout
    print(f"Invalidation requested already exist, try a unique caller reference: {e}")

# except exception as e1:
#     # Throws any other exceptions occured at runtime.
#     print(f"An error occured: {e1}")