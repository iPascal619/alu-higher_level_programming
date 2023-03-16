#!/usr/bin/python3
"""creates a class Node and defines it methods"""


class Node:
    """defines data and next node methods"""

    def __init__(self, data, next_node=None) -> None:
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value

"""creates a singly linked list class and its methods"""


class SinglyLinkedList:
    """defines a private instance attribute head"""
    def __init__(self) -> None:
        self.__head = None

    def sorted_insert(self, value):
        """insert new node"""
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        else:
            tmp = self.__head
            if tmp.data > new_node.data:
                new_node.next_node = tmp
                self.__head = new_node
                return
            while tmp.next_node is not None:
                tmp2 = tmp.next_node
                if tmp2.data < new_node.data:
                    tmp = tmp2
                else:
                    new_node.next_node = tmp.next_node
                    tmp.next_node = new_node
                    return
            tmp.next_node = new_node

    def stringrep(self):
        strrep = ""
        tmp = self.__head
        while tmp is not None:
            datavalue = tmp.data
            strrep = strrep + str(datavalue)
            tmp = tmp.next_node
            if tmp:
                strrep = strrep + "\n"
        return strrep

    def __repr__(self):
        return(self.stringrep())
