#!/usr/bin/python3

"""This is a class of Node of a Signly Linked List"""


class Node:
    """This class contains data, and an address of next node"""

    def __init__(self, data, next_node=None):
        """Initialize new node with data and next_node
            Args:
                data (int): the data of node instance.
                next_node (Node): the pointer of next node pointer.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """This is a getter method, that returns the address
        of data of current object.
        """
        return (self.__data)

    @data.setter
    def data(self, value):
        """This is a setter method, that sets the value of data."""
        if (not isinstance(value, int)):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """This is a getter method, that returns the address
        of next_node object.
        """
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """This is a setter method, that is sets the value of
        next_node.
        """
        if (not isinstance(value, Node) and value is not None):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


"""This is the class of Singly Linked List."""


class SinglyLinkedList:
    """Singly Linked List, that contains attributes and methods,
    that helps to create sequence of nodes related with each other."""

    def __init__(self):
        """Initializing the head pointer with None value.
            Args:
                head (Node): the pointer that contains the head
                node.
        """
        self.__head = None

    def sorted_insert(self, value):
        """This method inserts new node into the correct sorted position
        in the list.
            Args:
                value (Node): the new node in the right position.
        """

        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Prints the Singly Linked List content."""
        values = []
        head = self.__head
        while (head is not None):
            values.append(str(head.data))
            head = head.next_node
        return ("\n".join(values))
