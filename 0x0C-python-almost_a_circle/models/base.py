#!/usr/bin/python3
"""
Module that defines a base class
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON string representation of an instance"""
        if (not list_dictionaries or list_dictionaries is None):
            return ("[]")
        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes JSON string representation of a list of instnaces to a file
        """
        list_dict = []
        for object_ in list_objs:
            list_dict.append(object_.to_dictionary())

        dictionary = cls.to_json_string(list_dict) if \
            list_objs is not None else []
        name = cls.__name__ + ".json"

        with open(name, 'w') as file_1:
            file_1.write(dictionary)
