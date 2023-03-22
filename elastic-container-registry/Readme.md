<!--BEGIN STABILITY BANNER-->
---

![Stability: Stable](https://img.shields.io/badge/stability-Stable-success.svg?style=for-the-badge)

> **This is a stable example. It should successfully build out of the box**
>
> This example is built on boto3 libraries marked "Stable" and does not have any infrastructure prerequisites to build.
---
<!--END STABILITY BANNER-->

## Batch PUT Lifecycle Policy
---
**👉 What does this script do?**

Allows you to do the following:

1. Place an ecr lifecycle_policy **rule** to all your repositories based on a specific **tags** placed ecr repo.
2. Put **multiple tags** on ecr repos based on various environments.
3. Reduce your ecr image storage cloudspends.



**🤚 What does this doesn't do?**
Currently this script doesn't allow to do the following:

1. Place multiple ecr lifecycle_policy based **rules** for now
2. Cannot paginate for now.
3. Code isn't optimized yet, it lacks reusability for now.

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