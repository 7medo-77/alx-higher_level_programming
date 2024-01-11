#!/usr/bin/python3
def weight_average(my_list=[]):
    if (len(my_list) == 0 or not my_list):
        return (0)
    num_dict = dict(my_list)
    sum_weight = 0
    sum_score = 0
    weighted_average = 0

    for key, value in num_dict.items():
        sum_score += (int(key) * value)
        sum_weight += value
    weighted_average = float(sum_score / sum_weight)

    return (weighted_average)
