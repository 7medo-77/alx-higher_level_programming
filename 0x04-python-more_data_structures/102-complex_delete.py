#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dic = a_dictionary.copy()
    hash_list = []
    for key, value_1 in new_dic.items():
        if (value == value_1):
            hash_list.append(key)
    for i in hash_list:
        del a_dictionary[i]
    new_dic = a_dictionary.copy()
    return (new_dic)
