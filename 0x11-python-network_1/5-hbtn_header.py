#!/usr/bin/python3
"""Python script which fetches a link and returs the HTTP response body"""
import requests


if __name__ == "__main__":
    r = requests.get("https://alx-intranet.hbtn.io/status")
    print(r.headers['X-Request-Id'])
