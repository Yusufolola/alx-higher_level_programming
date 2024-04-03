#!/usr/bin/python3
"""class tha define a student"""


import json
class Student:
    """class that define a student"""
    
    def __init__(self, first_name, last_name, age):
        """class that define a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns a json representation"""

        return vars(self).copy()          
