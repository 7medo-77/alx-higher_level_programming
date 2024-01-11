#!/usr/bin/python3
def best_score(a_dictionary):
    if (not a_dictionary):
        return (None)
    max = list(a_dictionary.values())[0]
    key_max = list(a_dictionary.keys())[0]

    for key, value in a_dictionary.items():
        if (value > max):
            key_max = key

    return (key_max)
