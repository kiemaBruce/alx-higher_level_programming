#!/usr/bin/python3
"""Takes a URL, sends a request to the URL and displays the value of the
X-Request-Id variable found in the header of the response."""

import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        page_info = response.info()
        print(page_info.get('X-Request-Id'))
