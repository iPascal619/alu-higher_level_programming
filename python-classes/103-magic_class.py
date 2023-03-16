#!/usr/bin/python3
"""create a class MagicClass"""


import math


class MagicClass:
    """defines initiation, area and circumfrence methods"""
    def __init__(self, radius=0) -> None:
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        return ((self.__radius ** 2) * (math.pi))

    def circumference(self):
        return (2 * (math.pi) * self.__radius)
