#!/usr/bin/python3
import random
list_random = []
i = 0
for i in range(0, 10):
    list_random.append(random.randint(1, 10))
print(list_random)
print("{:d}".format(i))

index = i
while (index > 0):
    inner = 0
    while (inner < index):
        if (list_random[inner] > list_random[inner + 1]):
            temp = list_random[inner]
            list_random[inner] = list_random[inner + 1]
            list_random[inner + 1] = temp
        else:
            pass
        inner += 1
    index -= 1
print(list_random)
