import os
import time
import boto3
import botocore.exceptions
from datetime import datetime

# Fetch current datetime.
current = datetime.now()

# Fetch DistributionId from environment variables.
id = os.environ['CLOUDFRONT_DISTRIBUTION_ID']
path = os.environ['S3_OBJECT_INVALIDATION_KEY']


def lambda_handler(event, context):

    """event: codepipeline job
       context: runtime environment for lambda function, i.e., python 3.9
    """

    # Set path
    print(path)

    # Use client
    client = boto3.client('cloudfront')

    try:
        # Create Invalidation Request
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

        print(response_dict)

        # Fetch current invalidation status
        get_response_dict = client.get_invalidation(

            DistributionId = id,
            Id = response_dict.get('Invalidation').get('Id')

        )

        # Confirm invalidation
        print(f"Invaldation completed successfully: {get_response_dict}")

        # Creates client for codepipeline.
        code_pipeline = boto3.client('codepipeline')

        # Get the job id of current codepipeline action.
        job_id = event.get('CodePipeline.job').get('id')

        print(f"Current codepipeline in execution with id: {job_id}")        

        # Use code_pipeline client to call put_job_success_result()
        code_pipeline.put_job_success_result(jobId = job_id)

    except (botocore.exceptions.ClientError, Exception) as e:
        print(f"An exception was raised with following message: {e}")

        # Create client
        code_pipeline = boto3.client('codepipeline')

        # Get job id
        job_id = event.get('CodePipeline.job').get('id')

        # Instruct Codepipeline to mark the `action` as failure.
        code_pipeline.put_job_failure_result(
            jobId = job_id,
            failureDetails = {
                'type': 'JobFailed',
                'message': str(e),
                'externalExecutionId': context.aws_request_id # unique identifier for each new lambda function invocation.
            }
        )

    finally:
        # Skip
        pass