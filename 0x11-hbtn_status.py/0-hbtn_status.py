#!/usr/bin/python3
"""Python script which fetches a link and returs the HTTP response body"""


import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    res = response.read()
print(res)
