#!/usr/bin/python3
"""Python script which fetches a link and returs the HTTP response body"""


import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    res = response.read()
    type_res = type(res)
print("""Body response:
\t- type: {}
\t- content: {}
\t- utf8 content: {}""".format(type_res, res, res.decode("utf-8")))
