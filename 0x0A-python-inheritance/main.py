#!/usr/bin/python3
# is_same_class = __import__('2-is_same_class').is_same_class
#
# a = 1
# if is_same_class(a, int):
#     print("{} is an instance of the class {}".format(a, int.__name__))
# if is_same_class(a, float):
#     print("{} is an instance of the class {}".format(a, float.__name__))
# if is_same_class(a, object):
#     print("{} is an instance of the class {}".format(a, object.__name__))
#
#
MyList = __import__('1-my_list').MyList

my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)
print(my_list)
my_list.print_sorted()
print(my_list)

# lookup = __import__('0-lookup').lookup
#
# class MyClass1(object):
#     pass
#
# class MyClass2(object):
#     my_attr1 = 3
#     def my_meth(self):
#         pass
#
# print(lookup(MyClass1))
# print(lookup(MyClass2))
# print(lookup(int))
