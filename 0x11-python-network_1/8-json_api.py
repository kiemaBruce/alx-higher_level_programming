#!/usr/bin/python3
"""
Takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]
    url = "http://0.0.0.0:5000/search_user"
    r = requests.post(url, data={"q": q})

    if len(r.text) == 3:
        if r.text[0] == '{' and r.text[1] == '}' and \
                r.text[2] == '\n':
            print("No result")
    else:
        try:
            decoded_json = r.json()
            print(f"[{decoded_json.get('id')}] {decoded_json.get('name')}")
        except Exception as e:
            print("Not a valid JSON")
