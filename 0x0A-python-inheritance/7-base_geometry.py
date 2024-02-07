#!/usr/bin/python3
"""
Module that defines a class Base Geometry
"""


class BaseGeometry:
    """
    BaseGeometry class which forms the base class for different
    child classes
    """
    def __init__(self):
        return

    """
    Function that raises exception
    """
    def area(self):
        raise Exception("area() is not implemented")

    """
    Function that raises exception
    """
    def integer_validator(self, name, value):
        if (not isinstance(value, int)):
            raise TypeError("{} must be an integer".format(name))
        elif (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
