#!/usr/bin/python3
from sys import argv

i = 1
sum = 0
while (i < len(argv)):
    sum += eval(argv[i])
    i += 1
print(sum)
