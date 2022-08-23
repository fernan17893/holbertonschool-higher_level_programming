#!/usr/bin/python3
# Script takes Python credentials and displays id

import sys
import requests


if __name__ == "__main__":

    r = requests.get('https://api.github.com/user', auth=(sys.argv[1],sys.argv[2]))
    rson = r.json()

    print(rson.get("id"))
