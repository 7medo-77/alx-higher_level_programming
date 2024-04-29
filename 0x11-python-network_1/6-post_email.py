#!/usr/bin/python3
"""Python script which fetches a link and returs the HTTP response body"""
import requests
import sys


if __name__ == "__main__":
    data = {"email" : sys.argv[2]}
    r = requests.post(sys.argv[1], data)
    print("Your email is: {}".format(r.text) )
