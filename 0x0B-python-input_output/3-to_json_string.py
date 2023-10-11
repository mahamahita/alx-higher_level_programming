#!/usr/bin/python3
""" a function that returns the JSON representation of an object (string) """
import json


def to_json_string(my_obj):
    """
    to_json_string - returns the JSON representation of an object (string):
    Args:
        my_obj: string to represent
    Return: json representation
    """
    return json.dumps(my_obj)
