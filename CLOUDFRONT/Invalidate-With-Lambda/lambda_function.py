import os
import boto3
import botocore.exceptions
from datetime import datetime

# Fetch current datetime.
current = datetime.now()

# Fetch DistributionId from environment variables.
id = os.environ['CLOUDFRONT_DISTRIBUTION_ID']

try:

    def lambda_handler(event, context):

        ## Initialize empty list for object keys
        # Uncomment when dealing with multiple objects at the bucket folder. 
        # object_keys = []
        
        # For each 'Record' (dictionary) event of type S3, fetch S3 bucket object's -> key
        for record in event['Records']:

            s3 = record.get('s3')
            s3_object = s3.get('object')
            object_key = s3_object.get('key')
            
            # Append object key to list
            path = f"/{object_key}"
        
        # # Create invalidation batch ...
        # # Uncomment when dealing with multiple objects at the bucket folder.
        # paths = {
        #     'Quantity': len(object_keys),
        #     'Items': [f"/{key}" for key in object_keys]
        # }
        
        # Print paths to stdout
        print(path)
        
        # Use client
        client = boto3.client('cloudfront')

        try:
            # Create invalidation request
            response_dict = client.create_invalidation(

                DistributionId = id,
                InvalidationBatch = {
                
                    'Paths': {
                        'Quantity': 1,
                        'Items': [path]

                    },
                    'CallerReference': str(current)

                }
            )

            # Output response from cloudfront
            print(response_dict)

        except botocore.exceptions.ClientError as e:
            # Throw exception error message at stdout
            print(f"An exception was raise with message: {e}")

        except Exception as e1:
            raise e1

except Exception as e2:
    raise e2
