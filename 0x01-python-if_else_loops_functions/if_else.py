#!/usr/bin/python3

name = "Ahmed"
age = 26

if (age >= 18):
    print("what")
else:
    print("ever")

def function_first(a, b):
    if (a > b):
        print("First paramter is greater than second")
    elif (a == b):
        print("Two paramters are equal")
    else:
        print("Second paramter is greater than the first")
    return(1)

number = function_first(5,22)
print(number)
