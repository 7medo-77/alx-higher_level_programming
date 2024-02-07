#!/usr/bin/python3
import os
import sys

Student = __import__('11-student').Student
read_file = __import__('0-read_file').read_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

path = sys.argv[1]

if os.path.exists(path):
    os.remove(path)

student_1 = Student("John", "Doe", 23)
j_student_1 = student_1.to_json()
print("Initial student:")
print(student_1)
print(type(student_1))
print(type(j_student_1))
print("{} {} {}".format(student_1.first_name, student_1.last_name, student_1.age))


save_to_json_file(j_student_1, path)
read_file(path)
print("\nSaved to disk")


print("Fake student:")
new_student_1 = Student("Fake", "Fake", 89)
print(new_student_1)
print(type(new_student_1))
print("{} {} {}".format(new_student_1.first_name, new_student_1.last_name, new_student_1.age))


print("Load dictionary from file:")
new_j_student_1 = load_from_json_file(path)

new_student_1.reload_from_json(j_student_1)
print(new_student_1)
print(type(new_student_1))
print("{} {} {}".format(new_student_1.first_name, new_student_1.last_name, new_student_1.age))


# Student = __import__('10-student').Student
#
# student_1 = Student("John", "Doe", 23)
# student_2 = Student("Bob", "Dylan", 27)
#
# j_student_1 = student_1.to_json()
# j_student_2 = student_2.to_json(['first_name', 'age'])
# j_student_3 = student_2.to_json(['middle_name', 'age'])
#
# print(j_student_1)
# print(j_student_2)
# print(j_student_3)


# load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
#
# filename = "my_list.json"
# my_list = load_from_json_file(filename)
# print(my_list)
# print(type(my_list))
#
# filename = "my_dict.json"
# my_dict = load_from_json_file(filename)
# print(my_dict)
# print(type(my_dict))
#
# try:
#     filename = "my_set_doesnt_exist.json"
#     my_set = load_from_json_file(filename)
#     print(my_set)
#     print(type(my_set))
# except Exception as e:
#     print("[{}] {}".format(e.__class__.__name__, e))
#
# try:
#     filename = "my_fake.json"
#     my_fake = load_from_json_file(filename)
#     print(my_fake)
#     print(type(my_fake))
# except Exception as e:
#     print("[{}] {}".format(e.__class__.__name__, e))
#

# save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
#
# filename = "my_list.json"
# my_list = [1, 2, 3]
# save_to_json_file(my_list, filename)
#
# filename = "my_dict.json"
# my_dict = { 
#     'id': 12,
#     'name': "John",
#     'places': [ "San Francisco", "Tokyo" ],
#     'is_active': True,
#     'info': {
#         'age': 36,
#         'average': 3.14
#     }
# }
# save_to_json_file(my_dict, filename)
#
# try:
#     filename = "my_set.json"
#     my_set = { 132, 3 }
#     save_to_json_file(my_set, filename)
# except Exception as e:
#     print("[{}] {}".format(e.__class__.__name__, e))
#
# to_json_string = __import__('3-to_json_string').to_json_string
#
# my_list = [1, 2, 3]
# s_my_list = to_json_string(my_list)
# print(s_my_list)
# print(type(s_my_list))
#
# my_dict = { 
#     'id': 12,
#     'name': "John",
#     'places': [ "San Francisco", "Tokyo" ],
#     'is_active': True,
#     'info': {
#         'age': 36,
#         'average': 3.14
#     }
# }
# s_my_dict = to_json_string(my_dict)
# print(s_my_dict)
# print(type(s_my_dict))
#
# try:
#     my_set = { 132, 3 }
#     s_my_set = to_json_string(my_set)
#     print(s_my_set)
#     print(type(s_my_set))
# except Exception as e:
#     print("[{}] {}".format(e.__class__.__name__, e))
#
#
# write_file = __import__('1-write_file').write_file
#
# nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
# print(nb_characters)


# read_file = __import__('0-read_file').read_file
#
# read_file("my_file_0.txt")
