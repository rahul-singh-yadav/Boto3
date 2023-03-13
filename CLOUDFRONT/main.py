import boto3
import os
import dotenv
from datetime import date

# Load environment variables from .env
dotenv.load_dotenv()

# Fetch current datetime.
current = date.today()

# Use client()
client = boto3.client('cloudfront')

# Fetch DistributionId from environment variables.
id = os.environ.get('CLOUDFRONT_ID')

# Fetch invalidation path from environemnt variables.
path = os.environ.get('INVALIDATION_PATH')


# Save responses
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