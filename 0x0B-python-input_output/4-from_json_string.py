#!/usr/bin/python3
"""returns an object rep by json string"""


import json
def from_json_string(my_str):
    """returns python obj"""

    return json.loads(my_str)
