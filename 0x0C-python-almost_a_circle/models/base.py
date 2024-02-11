#!/usr/bin/python3
"""
Module that defines a base class
"""


class Base:
    """
    Base parent class from which all child classes will inherit
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if (id is None):
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects
        else:
            self.id = id
