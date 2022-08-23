#!/usr/bin/python3
"""Script takes Python credentials and displays id"""
import sys
import requests


if __name__ == "__main__":
    base = HTTPBasicAuth(sys.argv[1], sys.argv[2])
r = requests.get("https://api.github.com/user", auth=base)
print(r.json().get("id"))
