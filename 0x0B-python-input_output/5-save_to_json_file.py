#!/usr/bin/python3
"""
Module that encodes a JSON string and writes it to a file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Method that encodes a JSON string and writes it to a file
    """
    json_text = json.dump(my_obj)
    with open(filename, 'w') as file_1:
        return(file_1.write(json_text))
