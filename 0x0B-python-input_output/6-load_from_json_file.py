#!/usr/bin/python3
"""Create object from a JSON file"""
import json


def load_from_json_file(filename):
    """create object from JSON file"""
    with open(filename, encoding="utf-8")as f:
        return json.load(f)
