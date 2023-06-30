#!/usr/bin/python3

"""Addition function, that adds two numbers and returns the result"""


def add_integer(a, b=98):
    """
        This function adds two numbers, and resturns the result,
        but first it checks the type of paramters if integers or foloats
        othwerwise it raises an Error of Type 'TypeError'.

        >>> add_integer(15, 5)
        20
        >>> add_integer('a', 5)
        TypeError: a must be an integer
        >>> add_integer(10.5, 12)
        22

        Args:
            a (int or float): this is first number.
            b (int or float): this is second number.

        Return:
            returns the summation of these two numbers.
    """
    if not a or (type(a) != int and type(a) != float):
        raise TypeError("a must be an integer")
    if (type(b) != int and type(b) != float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
