#!/bin/bash
# Sends requests to a URL as an argument and displays only status code
curl -s -o /dev/null -w "%{http_code}" "$1"
