#!/usr/bin/python3
"""Python script which fetches a link and returs the HTTP response body"""


import urllib.request
import sys
with urllib.request.urlopen(sys.argv[1]) as request:
    request.get_header(sys.argv[1])
    print(request)
