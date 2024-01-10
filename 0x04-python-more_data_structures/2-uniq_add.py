#!/usr/bin/python3
def uniq_add(my_list=[]):
    set_1 = set(my_list)
    new_list = list(set_1)

    rolling_sum = 0
    for i in new_list:
        rolling_sum += i
    return (rolling_sum)

