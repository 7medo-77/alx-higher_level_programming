#!/usr/bin/python3
for iter in range(0, 100):
    if (iter == 99):
        print("{:02d}".format(iter))
    else:
        print("{:02d}".format(iter), end=", ")
    iter += 1
