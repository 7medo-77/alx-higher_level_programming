#!/usr/bin/python3
"""Python script which fetches a link and returs the HTTP response body"""
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as request:
        try:
            response = request.read().decode('utf-8')
            print(response)
        except urllib.request.HTTPError as e:
            print("Error code: {}".format(e.code))
