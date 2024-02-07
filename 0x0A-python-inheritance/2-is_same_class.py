#!/usr/bin/python3
"""
Module that defines function
True if an object is an instance of the specified class
"""


def is_same_class(obj, a_class):
    """
    Function that checks if an object is of type a_class
    """
    return (type(obj) is a_class)
