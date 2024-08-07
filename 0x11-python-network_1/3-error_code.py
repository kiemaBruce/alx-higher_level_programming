#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and displays the body of the
response (decoded in utf-8)"""

import sys
import urllib.error
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
            decoded_body = body.decode('utf-8')
            print(decoded_body)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
