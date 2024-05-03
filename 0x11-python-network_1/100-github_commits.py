#!/usr/bin/python3
"""Python script which fetches a link and returs the HTTP response body"""
import requests
import sys


if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    url_string = "https://api.github.com/repos/" + owner_name + '/' + repo_name + "commits"
    # auth_tuple = (username, passwd)
    response = requests.request("GET",
                                url_string,)
    print(response.json().get('sha'))
