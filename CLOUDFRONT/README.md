## How to use this script
---

**Pre-requisites**:

Should have the following installed at your system:

- Python3 version: 3.10.10
- Pip3
- `aws-cli` : 2.6.0
- programatic access credentials with a default profile set.

### Steps
---
1. Run `pip3 freeze` to generate required packages at your environment.
2. Create a .env file with the following key:=value pairs:

    - CLOUDFRONT_ID
    - INVALIDATION_PATH

3. Run python script using `python main.py`