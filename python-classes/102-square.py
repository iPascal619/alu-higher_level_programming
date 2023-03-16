#!/usr/bin/python3
"""creates class square with private instance
    attribute size and public instance method"""


class Square:
    """Defines private instance attribute"""
    def __init__(self, size=0) -> None:
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of the square"""
        value = self.__size ** 2
        return value

    def __eq__(self, other) -> bool:   # equal
        return self.area() == other.area()

    def __lt__(self, other) -> bool:   # less than
        return self.area() < other.area()

    def __le__(self, other) -> bool:   # less than or equal to
        return self.area() <= other.area()
