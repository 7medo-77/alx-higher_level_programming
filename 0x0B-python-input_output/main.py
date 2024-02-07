#!/usr/bin/python3
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "my_list.json"
my_list = [1, 2, 3]
save_to_json_file(my_list, filename)

filename = "my_dict.json"
my_dict = { 
    'id': 12,
    'name': "John",
    'places': [ "San Francisco", "Tokyo" ],
    'is_active': True,
    'info': {
        'age': 36,
        'average': 3.14
    }
}
save_to_json_file(my_dict, filename)

try:
    filename = "my_set.json"
    my_set = { 132, 3 }
    save_to_json_file(my_set, filename)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

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
