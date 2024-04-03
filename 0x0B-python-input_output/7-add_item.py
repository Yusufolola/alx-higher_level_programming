#!/usr/bin/python3
"""a script that adds all arg to a list"""
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
import sys
import json

if __name__ == "__main__":

    filename = "add_item.json"
    try:
        argument = load_from_json_file(filename)

    except FileNotFoundError:
        argument = []
    argument.extend(sys.argv[1:])
    save_to_json_file(argument, filename)
