#!/usr/bin/python3
"""Python script which fetches a link and returs the HTTP response body"""
import urllib.request as request
import urllib.error as error
import sys


if __name__ == "__main__":
    response_obj = request.Request(sys.argv[1])
    with request.urlopen(sys.argv[1]) as response_obj:
        try:
            response = response_obj.read().decode('utf-8')
            print(response)
        except error.HTTPError as e:
            print("Error code: {}".format(e.code))