#!/usr/bin/python3
def uppercase(str):
    for a in str:
        if (ord(a) >= 97 and ord(a) <= 122):
            print("{}".format(chr((ord(a) - (ord('a') - ord('A'))))), end="")
        else:
            print("{}".format(a), end= "")
