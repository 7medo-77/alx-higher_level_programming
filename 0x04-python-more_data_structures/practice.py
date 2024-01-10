#!/usr/bin/python3
set_1 = {1,2,3,4,5,6}
set_2 = {2,6,7,8,9,10}

set_3 = set_1 | set_2
set_4 = set_1 & set_2

dictionary = {i : 2**i for i in range(0, 12)}
index = 0
for value in dictionary.values():
    if (index % 3 == 0 and index != 0):
        print()
    print(value, end="\t")
    index += 1
print(len(dictionary))
