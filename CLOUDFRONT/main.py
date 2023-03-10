import boto3
from datetime import date

# Fetch current datetime
current = date.today()

# Use client()
client = boto3.client('cloudfront')

# Save responses
response = client.create_invalidation(
    DistributionId='<ID>',
    InvalidationBatch={
        'Paths': {
            'Quantity': 1, 
            'Items': ['/createpataaminified/smart-city-create-pataa.js']
        },
        'CallerReference': str(current)
    }
)
