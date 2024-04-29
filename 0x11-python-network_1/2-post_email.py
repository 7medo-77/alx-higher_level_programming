#!/usr/bin/python3
"""Python script which fetches a link and returs the HTTP response body"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    values = {"email": sys.argv[2]}
    package = urllib.parse.urlencode(values)
    response_obj = urllib.request.Request(sys.argv[1], data=package)

    with urllib.request.urlopen(response_obj) as request:
        response = request.read().decode('utf-8')
    print("Your email is: {}".format(response))
