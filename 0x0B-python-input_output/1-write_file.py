#!/usr/bin/python3
"""
Module which writes a string of text into a file
"""


def write_file(filename="", text=""):
    """Function that writes onto the content of a file"""
    with open(filename, 'w') as file_1:
        sentence = text
        bytes = file_1.write(sentence)
        return (bytes)
