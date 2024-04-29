#!/usr/bin/python3
"""Python script which fetches a link and returs the HTTP response body"""
import requests
import sys


if __name__ == "__main__":
    param = {"q": sys.argv[1] if len(sys.argv) == 2 else ""}
    response = requests.post('http://0.0.0.0:5000/', param)
    try:
        if response.json():
            print("[{}] {}".format(response.json()['id'],
                                   response.json()['name']))
        else:
            print("No result")
    except requests.exceptions.JSONDecodeError:
        print("Not a valid JSON")
