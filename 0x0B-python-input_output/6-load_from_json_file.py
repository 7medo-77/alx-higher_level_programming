#!/usr/bin/python3
"""
Module that encodes a JSON string and writes it to a file
"""
import json


def load_from_json_file(filename):
    """
    Method that encodes a JSON string and writes it to a file
    """
    with open(filename, 'r+') as f:
        string = f.read()
        return (json.loads(string))
