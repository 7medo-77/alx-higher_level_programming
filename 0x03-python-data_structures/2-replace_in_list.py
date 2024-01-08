#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    my_list.insert(idx, element)
    del my_list[idx + 1]
    return(my_list)
