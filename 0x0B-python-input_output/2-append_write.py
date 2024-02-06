#!/usr/bin/python3
"""
Module which writes a string of text to the end of a file
"""


def append_write(filename="", text=""):
    """Function that appends onto the content of a file"""
    with open(filename, 'a') as file_1:
        sentence = text
        bytes = file_1.write(sentence)
        return (bytes)
