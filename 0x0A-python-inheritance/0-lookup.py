#!/usr/bin/python3
"""
Returns all methods and attributes of an object as a list
"""


def lookup(obj):
    """
    Function that returns a list of all object attributes and methods
    """
    return (list(obj.__dict__))
