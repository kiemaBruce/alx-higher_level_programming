#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status using urllib"""

import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") \
            as response:
        the_page = response.read()
    body_str = the_page.decode('utf-8')
    body_type = type(the_page)
    print("Body response:")
    print(f" - type: {body_type}")
    print(f" - content: {the_page}")
    print(f" - utf8 content: {body_str}")
