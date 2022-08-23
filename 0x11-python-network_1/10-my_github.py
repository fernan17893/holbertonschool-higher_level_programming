#!/usr/bin/python3
""" Script takes Python credentials and displays id """
import sys
import requests


if __name__ == "__main__":
    user = sys.argv[1]
    passw = sys.argv[2]
r = requests.get('https://api.github.com/user', auth=(user, passw))
print(r.json().get("id"))

HEY WHATS UP THIS IS CHRIS
