#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
a = 10
b = 5
print("{} + {} = {}".format(a, b, calculator_1.add(a, b)))
print("{} - {} = {}".format(a, b, calculator_1.sub(a, b)))
print("{} * {} = {}".format(a, b, calculator_1.mul(a, b)))
print("{} / {} = {}".format(a, b, int(calculator_1.div(a, b))))