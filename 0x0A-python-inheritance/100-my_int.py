#!/usr/bin/python3
"""myint inherit from int"""


class MyInt(int):
    """same as above"""

    def __eq__(self, other):
        if self is other:
            return True
        return False
