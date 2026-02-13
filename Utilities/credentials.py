import os

def get_credentials():
    username = os.getenv("ORANGEHRM_USERNAME")
    password = os.getenv("ORANGEHRM_PASSWORD")
    if not username or not password:
        raise ValueError("Missing ORANGEHRM_USERNAME or ORANGEHRM_PASSWORD environment variables")
    return username, password
