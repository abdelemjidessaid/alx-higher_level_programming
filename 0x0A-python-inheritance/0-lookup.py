#!/usr/bin/python3

""" Function that display all attributes of objects """


def lookup(obj):
    """
    Function that prints all attributes of an given object.
    
    Args:
		obj (object): the given object.

    Return: list of attributes.
    """
    return (dir(obj))