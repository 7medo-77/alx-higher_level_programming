#!/usr/bin/python3
"""
Module that defines a function to check if an object
is a subclass of another object given as paramter
"""


def inherits_from(obj, a_class):
    """
    Function that checks if obj is a subclasss of a_class
    """
    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
