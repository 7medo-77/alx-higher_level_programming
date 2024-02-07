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

    def to_json(self):
        return (self.__dict__)
