#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    res = []
    for i in range(len(tuple_a) if len(tuple_a) > len(tuple_b) else len(tuple_b)):
        res.append((0 if i >= len(tuple_a) else tuple_a[i]) +
            (0 if i >= len(tuple_b) else tuple_b[i]))
    new_tuple = tuple(i for i in res)
    return (new_tuple[0], new_tuple[1])
