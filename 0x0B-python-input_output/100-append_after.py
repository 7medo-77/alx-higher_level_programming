#!/usr/bin/python3
"""
module that defines function to search and insert in a file
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Function that searches and inserts text into a file
    """
    text = ""
    with open(filename) as r:
            for line in r:
                text += line
                if search_string in line:
                    text += new_string
    with open(filename, "w") as w:
        w.write(text)