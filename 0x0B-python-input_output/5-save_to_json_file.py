#!/usr/bin/python3
"""function that write an object to text file in json"""

import json
def save_to_json_file(my_obj, filename):
    """return a text file"""

    with open(filename, "w") as file:
        return json.dump(my_obj, file)
