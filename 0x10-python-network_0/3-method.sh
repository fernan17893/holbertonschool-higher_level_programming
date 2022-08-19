#!/bin/bash
#Takes in a URL and displays all HHTP methods
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-