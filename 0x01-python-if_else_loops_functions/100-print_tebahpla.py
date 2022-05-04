#!/usr/bin/python3
for i in reversed(range(98, 123, 2)):
    print("{:c}".format(i), end='')
    i -= 1
    j = i - 32
    print("{:c}".format(j), end='')
