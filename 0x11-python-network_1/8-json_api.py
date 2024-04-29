#!/usr/bin/python3
"""Python script which fetches a link and returs the HTTP response body"""
import requests
import sys


if __name__ == "__main__":
    param = {"q": sys.argv[1] if sys.argv[1] else ""}
    response = requests.post('http://0.0.0.0:5000/search_user', param)
    print(response.json())
