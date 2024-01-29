#!/usr/bin/python3
"""
Function to add two integers
"""


def add_integer(a, b=98):
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    elif not a:
        raise TypeError("add_integer() missing 1 required positional argument: 'a'")
    else:
        res = int(a) + int(b)
    return (res)


if __name__ == "__main__":
    import doctest
    doctest.testfile("./tests/0-add_integer.txt")

