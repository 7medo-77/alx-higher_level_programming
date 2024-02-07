#!/usr/bin/python3
"""
Module that defines function that determines if an object
is an instance of a class
"""


def is_kind_of_class(obj, a_class):
    """
    Function that determines if an object is an instance of a class
    """
    return (issubclass(obj, a_class))
