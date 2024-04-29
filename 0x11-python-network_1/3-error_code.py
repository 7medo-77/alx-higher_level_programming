#!/usr/bin/python3
"""Python script which fetches a link and returs the HTTP response body"""
import urllib.request as request
import urllib.error as error
import sys


if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as request:
        try:
            response = request.read().decode('utf-8')
            print(response)
        except error.HTTPError as e:
            print("Error code: {}".format(e.code))
