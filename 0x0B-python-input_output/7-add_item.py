#!/usr/bin/python3
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


list_arg = load_from_json_file("add_item.json")
for i in sys.argv:
    list_arg.append(i)

save_to_json_file(list_arg, "add_item.json")
