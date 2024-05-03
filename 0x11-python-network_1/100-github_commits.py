#!/usr/bin/python3
"""Python script which fetches a link and returs the HTTP response body"""
import requests
import sys


if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    url_string = "https://api.github.com/repos/" + owner_name + '/' \
        + repo_name + '/' + "commits"
    # auth_tuple = (username, passwd)
    response = requests.request("GET",
                                url_string,)
    list_json = []

    for index, response in enumerate(response.json()[0:10]):
        tuple_json = (response['sha'], response.get("commit")
                      .get("author").get("name"))
        list_json.append(tuple_json)

    # for index, response in enumerate(response.json()[-11:-1]):
    #     tuple_json = (response['sha'], response.get("commit")
    #                   .get("author").get("name"))
    #     list_json.append(tuple_json)


    # for index, element in enumerate(list_json):
    #     print("{} -> {}: {}".format(index + 1, element[0], element[1]))

    for index, element in enumerate(list_json):
        print("{}: {}".format(element[0], element[1]))
