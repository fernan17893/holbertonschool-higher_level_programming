#!/usr/bin/bash
# Sends requests to a URL as an argument and displays only status code
curl -sL -w "%{http_code}" "$1"
