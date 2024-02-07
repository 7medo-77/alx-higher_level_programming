#!/usr/bin/python3
"""
Module that encodes a JSON string and writes it to a file
"""
import json


def load_from_json_file(filename):
    """
    Method that encodes a JSON string and writes it to a file
    """
    json_text = json.dumps(my_obj)
    with open(filename, 'w') as file_1:
        file_1.write(json_text)
