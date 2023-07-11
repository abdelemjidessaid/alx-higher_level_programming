#!/usr/bin/python3

"""
    Class of Student
"""


class Student:
    """
        Class Student has public attributes:
            first_name (str): string of first name.
            last_name (str): string of last name.
            age (int): integer of age.
    """
    def __init__(self, first_name, last_name, age):
        """
            Student's constructor that initialize public attributes.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
            Function that returns the dictionary of current class's objects.
        """
        return (self.__dict__)

    def to_json(self, attrs=None):
        """
            Function that returns the dictionary of current class's objects
            using it's names.

            Args:
                attrs (list): contains the attributes that should return.
        """
        if (attrs is not None):
            res = {}
            for key in self.__dict__:
                if (key in attrs):
                    res[key] = self.__dict__[key]
            return (res)
        return (self.__dict__)

    def reload_from_json(self, json):
        """
            Function that update the current objects attribute
            from json dictionary.

            Args:
                json (dict): contains the new values
                attributes.
        """
        for key, value in json.keys():
            self.__dict__[key] = value
