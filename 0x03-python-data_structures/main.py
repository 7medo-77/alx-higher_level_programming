#!/usr/bin/python3
# 5-no_c.py
# no_c = __import__('5-no_c').no_c
#
# print(no_c("Best School"))
# print(no_c("Chicago"))
# print(no_c("C is fun!"))
multiple_returns = __import__('8-multiple_returns').multiple_returns

sentence = "At school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))
