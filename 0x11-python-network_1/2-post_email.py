#!/usr/bin/python3
""" Takes URL and sends POST with email as a parameter"""

import urllib.request
import sys
import urllib.parse

if __name__ == '__main__':
    url = sys.argv[1]
    values = {'email': sys.argv[2]}

    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf_8"))
