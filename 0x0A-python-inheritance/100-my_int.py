#!/usr/bin/python3
"""
Module which defines a class MyInt which is a child
class of the class int
"""


class MyInt(int):
    """
    MyInt child class, which has very peculiar rebelliousness
    """
    def __init__(self):
        """Constructor method inherited from parent int"""
        super().__init__()

    def __eq__(self, other):
        """rich comparison method == which is inverted to !="""
        if (self is other):
            return (False)

    def __ne__(self, other):
        """rich comparison method != which is inverted to =="""
        if (self is not other):
            return (False)
