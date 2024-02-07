#!/usr/bin/python3
"""
Module that encodes a JSON string and writes it to a file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Method that encodes a JSON string and writes it to a file
    """
    with open(filename, 'w', encoding="utf-8") as file_1:
        json_text = json.dumps(my_obj)
        file_1.write(json_text)
