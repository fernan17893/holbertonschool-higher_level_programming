#!/usr/bin/python3
""" Display value of header X-Request-Id """
import sys
import urllib.request 

if __name__ == '__main__':
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        print(response.getheader('X-Request-Id'))
