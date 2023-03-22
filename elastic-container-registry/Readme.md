## Batch PUT Lifecycle Policy
---
**Example Policy**:

```
{
    "rules": [
        {
            "rulePriority": 1,
            "description": "Keep only one untagged image, expire all others.",
            "selection": {
                "tagStatus": "untagged",
                "countType": "imageCountMoreThan",
                "countNumber": 1
            },
            "action": {
                "type": "expire"
            }
        }
    ]
}
```
### Pre-requisites
---
- AWS Cli must be installed, this code is tested on v2.6.0.
- AWS Profiles must be preconfigured.
- Python version 3.10.10

### Steps for running this script
---
1. Run `pip3` freeze at local machine.
2. Run `python main.py`

Note: lifecycle_policy.json must be present at cwd.

## Refrences
---
**Boto3 Documentation**
- At boto3  https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr/client/put_lifecycle_policy.html

**ECR Documentation**
- https://docs.aws.amazon.com/AmazonECR/latest/userguide/lifecycle_policy_examples.html
- https://docs.aws.amazon.com/AmazonECR/latest/userguide/ecr-using-tags.html