#!/usr/bin/python3

""" The base module """
import json
import csv
import turtle
import random


class Base:
    """
        The Base class of this package.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
            The constructor of Base class.

            Args:
                id (int): an id.
        """
        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    # --------------------- class methods -------------------------

    @classmethod
    def save_to_file(cls, list_objs):
        """
            Function that saves the JSON files from objects.

            Args:
                list_objs (list): list of objects.
        """
        if (list_objs is None):
            with open(f"{cls.__name__}.json", "w", encoding="utf-8") as file:
                file.write("[]\n")
        else:
            with open(f"{type(list_objs[0]).__name__}.json",
                      "w", encoding="utf-8") as file:
                file.write("[")
                for i in range(len(list_objs)):
                    file.write(
                        cls.to_json_string(list_objs[i].to_dictionary())
                        )
                    if (i < len(list_objs) - 1):
                        file.write(", ")
                file.write("]")

    @classmethod
    def create(cls, **dictionary):
        """
            Function that creates objects from dictionaries.

            Args:
                dictionary (dict): dictionary that contains all
                    object's attribute names and values.

            Return:
                instance with its attributes and values.
        """
        dummy = None
        if (cls.__name__ == "Rectangle"):
            dummy = cls(1, 1)
        if (cls.__name__ == "Square"):
            dummy = cls(1)
        dummy.update(**dictionary)
        return (dummy)

    @classmethod
    def load_from_file(cls):
        """
            Function that returns a list of instances.

            Return:
                list of instances.
        """
        # get the class name, which file name consists with it.
        file_name = f"{cls.__name__}.json"
        # try to open the file.
        try:
            with open(file_name, "r", encoding="utf-8") as file:
                json_code = file.read()
            dictionary = cls.from_json_string(json_code)
            instances = []
            for i in range(len(dictionary)):
                instances.append(cls.create(**dictionary[i]))
            return (instances)
        except Exception as e:
            return ([])

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
            Function that saves the list of objects as
            CSV File.

            Args:
                list_objs (list): list of objects.
        """
        dics = []
        for i in range(len(list_objs)):
            dics.append(cls.to_dictionary(list_objs[i]))
        with open(f"{cls.__name__}.csv", "w", encoding="utf-8") as file:
            headers = []
            if (cls.__name__ == "Rectangle"):
                headers = ["id", "width", "height", "x", "y"]
            if (cls.__name__ == "Square"):
                headers = ["id", "size", "x", "y"]
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(dics)

    @classmethod
    def load_from_file_csv(cls):
        """
            Function that loads objects from CSV File.

            Returns:
                list of instances
        """
        filename = "{:s}.csv".format(cls.__name__)
        a_list = []
        try:
            with open(filename, 'r') as a_file:
                reader = csv.DictReader(a_file)
                for row in reader:
                    for key in row:
                        row[key] = int(row[key])
                    a_list.append(row)
            list_instances = []
            for i in range(len(a_list)):
                list_instances.append(cls.create(**a_list[i]))
        except Exception as e:
            list_instances = []

        return list_instances

    # --------------------- static methods --------------------

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            Function that returns a JSON,
            String representation of list_dictionaries

            Args:
                list_dictionaries (dict): dictionary that contains
                an object attribute's names and its values.

            Return:
                JSON String that represents the given dictionary.
        """
        if (list_dictionaries is None or len(list_dictionaries) == 0):
            return ("[]")
        return (json.dumps(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """
            Function that create objects from string JSON code.

            Args:
                json_string (list): string contains JSON code.

            Return:
                list of objects.
        """
        return (json.loads(json_string))

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
            Function that draws shapes (Rectangle, Square).

            Args:
                list_rectangle (list): list of rectangle objects.
                list_square (list): list of square objects.
        """
        colors = [
            "red", "green", "blue", "black",
            "gray", "yellow", "purple"
            ]
        window = turtle.Turtle()
        window.pensize(3)

        # lets draw recrangles.
        for rectangle in list_rectangles:
            index = random.randint(0, len(colors) - 1)
            window.penup()
            window.goto(rectangle.x, rectangle.y)
            window.pendown()
            window.color(colors[index])
            for i in range(4):
                if (i == 1 or i == 3):
                    window.forward(rectangle.height)
                    window.left(90)
                else:
                    window.forward(rectangle.width)
                    window.left(90)

        # lets draw squares.
        for square in list_squares:
            index = random.randint(0, len(colors) - 1)
            window.penup()
            window.goto(square.x, square.y)
            window.pendown()
            window.color(colors[index])
            for i in range(4):
                window.forward(square.size)
                window.left(90)
        turtle.done()
