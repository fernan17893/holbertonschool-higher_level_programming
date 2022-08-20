#!/usr/bin/python3
""" Display value of header X-Request-Id """
import sys
from urllib.request import Request, urlopen

if __name__ == "__main__":
    with urlopen('https://intranet.hbtn.io/status') as response:
        pass
print(response.getheader('X-Request-Id'))
