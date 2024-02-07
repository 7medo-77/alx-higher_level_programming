#!/usr/bin/python3
"""
Module that defines a class Student which has three public instnace attributes
"""


class Student:
    """
    Initialization method
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    """
    Method that prints a filtered dictionary representation of an object
    """
    def to_json(self, attrs=None):
        if attrs is None:
            return (self.__dict__)
        else:
            dict_copy = self.__dict__.copy()
            dict_1 = {x: dict_copy.get(x) for x in attrs
                      if dict_copy.get(x) is not None}
            return (dict_1)

    """
    Method that replaces all attributes in 
    object with attributes from json file
    """
    def reload_from_json(self, json):
        for key, value in json.items():
            if self.key == key:
                self.value = value
        # self.first_name = json.get("first_name")
        # self.last_name = json.get("last_name")
        # self.age = json.get("age")
