#!/usr/bin/python3
import json
"""
Module which prints the JSON string representation of an object
"""


def to_json_string(my_obj):
    """Function that prints json string representation of an object"""
    return (json.dumps(my_obj))
