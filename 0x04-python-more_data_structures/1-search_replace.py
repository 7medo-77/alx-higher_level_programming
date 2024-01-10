#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    index = 0
    for i in new_list:
        if (i == search):
            new_list.insert(index, replace)
            del new_list[index + 1]
        index += 1
    return (new_list)
