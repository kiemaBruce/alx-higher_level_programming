#!/usr/bin/python3
"""Takes your GitHub credentials (username and password) and uses the GitHub
API to display your id"""

import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    url = f"https://api.github.com/users/{username}"
    headers = {"Authorization": f"token {token}"}
    r = requests.get(url, headers=headers)
    decoded_r = r.json()
    print(decoded_r.get('id'))
