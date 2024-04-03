#!/usr/bin/python3
"""returns the dictionary description"""


import json
def class_to_json(obj):
    """function that returns the dictionary of a class"""

    return json.dumps(vars(obj))

