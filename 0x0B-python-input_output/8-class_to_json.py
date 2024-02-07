#!/usr/bin/python3
"""
Module that returns dictionary description of an object
"""


def class_to_json(obj):
    """
    Method that returns a dictionary as a JSON serialization of an object
    """
    return (obj.__dict__)
