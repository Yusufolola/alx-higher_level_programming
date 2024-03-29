#!/usr/bin/python3
"""myint inherit from int"""


class MyInt(int):
    """same as above"""

    def __init___(self, value):
        super().__init__(value)

    def __eq__(self, other):
        if isinstance(other, MyInt):
