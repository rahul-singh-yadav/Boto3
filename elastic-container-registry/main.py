import os
import json
import boto3
import time
import botocore.exceptions

# Sets filepath
filepath = os.path.join(os.getcwd(), 'repositories.txt')

# Creates a client to interact with service 'ecr'
client = boto3.client('ecr')

# repositories : type(dict)
# key: 'repositories'; using dict. indexing
repositories_list = client.describe_repositories()['repositories']

# Open file for writing fetched data.
with open(filepath, "a") as file:

    # Loop through all repos and get repository names
    for repository in repositories_list:

        repository_name = repository.get('repositoryName')
        repository_uri = repository.get('repositoryUri')
        registry_id = repository.get('registryId')

        # Write to a file, if the file doesn't exist... create it.
        file.write(str(f"{repository_name}, {repository_uri}") + str('\n'))

# Post writing to file, close file.    
file.close()

print(f"Data written at {os.path.join(os.getcwd(), 'requirements.txt')} \n")

# Read lifecycle policy
print(f"Opening lifecycle policy rules file at {os.path.join(os.getcwd(), 'requirements.txt')} \n")
policy_data = open('./lifecycle_policy.json', "r")

rules = policy_data.read()

print(f"Current set of rules are: \n {rules}")

for rules in repositories_list:
    client.put_lifecycle_policy(

        registryId = str(rules.get('registryId')),
        repositoryName = str(rules.get('repositoryName')),
        lifecyclePolicyText = str(rules)
    )

time.sleep(3)

print(f"Closing file now...  \n")

policy_data.close()