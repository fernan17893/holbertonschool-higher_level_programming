#!/bin/bash
# Script takes URL, displays size of body
curl -s "$1" | wc -c
