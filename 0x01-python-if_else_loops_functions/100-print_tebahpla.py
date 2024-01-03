#!/usr/bin/python3

for a in range(26, 0, -1):
    if (a % 2 == 0):
        a += 96
    else:
        a += 64
    print("{}".format(chr(a)), end="")

    if (a % 2 == 0):
        a -= 96
    else:
        a -= 64

