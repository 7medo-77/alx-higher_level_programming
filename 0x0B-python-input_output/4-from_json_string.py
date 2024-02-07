#!/usr/bin/python3
"""
Module which prints the JSON string representation as a string
"""
import json


def from_json_string(my_str):
    """Function that prints json string representation as a string"""
    return (json.loads(my_str))
