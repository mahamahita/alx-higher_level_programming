#!/usr/bin/python3
""" a function that creates an Object from a “JSON file”"""

import json


def load_from_json_file(filename):
    """
    load_from_json_file - loads an object from JSON file.
    Args:
        filename: name of the file
    """
    with open(filename, "r") as f:
        my_obj = json.load(f)
        return my_obj
