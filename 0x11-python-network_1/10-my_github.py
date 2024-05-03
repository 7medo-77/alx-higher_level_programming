#!/usr/bin/python3
"""Python script which fetches a link and returs the HTTP response body"""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    passwd = sys.argv[2]
    auth_tuple = (username, passwd)
    # headers = {'Authorization': passwd}
    response = requests.request("GET", 'https://api.github.com/user', auth=auth_tuple)
    # print(json.dumps(response.json(), indent=4))
    print(response.json().get('id'))
