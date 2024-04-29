#!/usr/bin/python3
"""Python script which fetches a link and returs the HTTP response body"""
import requests


if __name__ == "__main__":
    # r = requests.get("https://alx-intranet.hbtn.io/status")
    # print("Body response:")
    # print("\t- type: {}".format(type(r.text)))
    # print("\t- content: {}".format(r.text))

    response = requests.get('https://alx-intranet.hbtn.io/status')
    print("""Body response:
    \t- type: {}
    \t- content: {}""".format(type(response.text), response.text))
