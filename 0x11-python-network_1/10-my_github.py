#!/usr/bin/python3
# Script takes Python credentials and displays id

import sys
from requests.auth import HTTPBasicAuth
import requests


if __name__ == "__main__":
    basic = HTTPBasicAuth(sys.argv[1], sys.argv[2])

    r = requests.get('https://api.github.com/user', auth=basic)
    rson = r.json()

    print(rson.get("id"))
