#!/usr/bin/python3
"""function that create obj from json file"""

import json
def load_from_json_file(filename):
    """create obj from json file"""

    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
