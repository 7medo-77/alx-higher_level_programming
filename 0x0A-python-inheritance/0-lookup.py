#!/usr/bin/python3
"""
Returns all methods and attributes of an object as a list
"""


def lookup(obj):
    return (list(obj.__dict__))
