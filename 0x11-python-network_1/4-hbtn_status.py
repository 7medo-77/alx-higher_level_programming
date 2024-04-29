#!/usr/bin/python3
"""Python script which fetches a link and returs the HTTP response body"""
import requests


if __name__ == "__main__":
    response = requests.get('https://alx-intranet.hbtn.io/status')
    print("""Body response:
    \t- type: {}
    \t- content: {}""".format(type(response.text), response.content))
