import os
import json
import boto3
import botocore.exceptions
from datetime import datetime

""" 1. Sets filepath for a text file that will be created.
    2. Creates a boto3 client to interact with ecr api.
    3. Fetches a dictionary containing all repositories at aws account in a region.
       # key: 'repositories'; using dict. indexing
    4. Logs message for file ready to be opened and written to at stdout.

    Note: The aws account and region are set using aws config profiles.
"""

filepath = os.path.join(os.getcwd(), 'repositories.txt')

client = boto3.client('ecr')

repositories_dict = client.describe_repositories()['repositories']

print(f"Opening file for writing fetched data.\n")

with open(filepath, "a") as file:
    """ 1. File is opened using context manager as 'file'.
        2. Writes current date-time to file for each successfull PUT job.
        3. Goes through all repositories in `repository_dict` object & sets them as:
            - Respository names.
            - Repository URIs.
            - Registry Id's. 
        4. Closes the file once data is written in the file named `requirements.txt` at cwd.

        Note: If the files doesn't exist, it creates one and writes data to it.
    """

    file.write(str(f"Last succesfull write: [{datetime.now()}] \n"))

    for repository in repositories_dict:

        repository_name = repository.get('repositoryName')
        repository_uri = repository.get('repositoryUri')
        registry_id = repository.get('registryId')

        file.write(str(f"{repository_name}, {repository_uri}") + str('\n'))

file.close()

print(f"Data written at {os.path.join(os.getcwd(), 'requirements.txt')} \n")

print(f"Opening lifecycle policy rules file at {os.path.join(os.getcwd(), 'requirements.txt')} \n")

with open('./lifecycle_policy.json', "r") as policy_data:
    """ 1. Opens a file containing ecr lifecycle policy as json data.
        3. Reads the json data to a variable named `rule`.
        2. Goes through all repositories in `repository_dict` objects.
        3. Inside the loop, calls put_lifecycle_policy method using `client` object and PUTS the following:
            - registryId
            - repositoryName
            - rule
        4. Closes the file post each successfull PUT job.
    """
    rule = policy_data.read()

    print(f"Current set of rules are: \n \n {rule} \n")

    for rules in repositories_dict:

        response = client.put_lifecycle_policy(

            registryId = str(rules.get('registryId')),
            repositoryName = str(rules.get('repositoryName')),
            lifecyclePolicyText = str(rule)
        )

    print(f"Closing file now...")

policy_data.close()
