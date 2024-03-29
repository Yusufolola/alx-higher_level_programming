#!/usr/bin/python3
""" a class that prints the list,but sorted"""


class MyList(list):
    """class"""

    def print_sorted(self):
        """prototype of the public method that sort the list"""

        print(sorted(self))
