#!/usr/bin/python3
"""Takes in a URL and an email, sends a POST request to the passed URL with the
email as a parameter, and displays the body of the response (decoded in utf-8)
"""

import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    values = {'email': email}
    data = urllib.parse.urlencode(values)
    data.encode('ascii')
    with urllib.request.urlopen(url) as response:
        body = response.read()
        decoded_body = body.decode('utf-8')
        print(decoded_body)
