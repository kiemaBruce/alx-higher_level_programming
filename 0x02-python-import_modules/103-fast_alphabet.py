#!/usr/bin/python3
import requests, bs4, re
print(re.sub('(<html>)|({})'.format('</html>\s*'), '', (requests.get('https://kiemabruce.github.io/uppercase-alphabet/')).text))
