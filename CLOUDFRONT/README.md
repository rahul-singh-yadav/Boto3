## How to use this script
---

**Prequisites**:

Should have the following installed at your system:

- Python3 version 3.10.10
- Pip3


### Steps
---
1. Run `pip3 freeze` to generate required packages at your environment.
2. Create a .env file with the following key's:
    - CLOUDFRONT_ID=<CloudFront-Distribution-ID>
    - INVALIDATION_PATH=<Path-For-S3-Bucket-Object>
3. Run python script using `python main.py`


