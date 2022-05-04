#!/usr/bin/python3
def remove_char_at(str, n):
    s2 = ""
    for i in range(len(str)):
        if i == n:
            continue
        s2 += str[i]
    return (s2)
