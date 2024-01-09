#!/usr/bin/python3
# 5-no_c.py
# no_c = __import__('5-no_c').no_c
#
# print(no_c("Best School"))
# print(no_c("Chicago"))
# print(no_c("C is fun!"))
add_tuple = __import__('7-add_tuple').add_tuple

tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))
