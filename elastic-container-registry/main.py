import os
import json
import boto3
import botocore.exceptions

# Create a client to interact with service 'ecr'
client = boto3.client('ecr')

# repositories : type(dict)
repositories = client.describe_repositories()['repositories']

# Loop through all repos and get repository names
for repository in repositories:
    repository_names = repository.get('repositoryName')
    registry_id = repository.get('registryId')

    # Return as a tuple of values
    print((repository_names, registry_id))