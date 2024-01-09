#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list.copy()
    index = 0
    for i in new_list:
        if (i % 2 == 0):
            new_list.insert(index, True)
            del new_list[index + 1]
        else:
            new_list.insert(index, False)
            del new_list[index + 1]
        index += 1
    return (new_list)
