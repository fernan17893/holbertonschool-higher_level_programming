#!/usr/bin/python3
for number in range(100):
    num = number % 10
    num2 = number // 10
    if number != 99:
        print("{:d}{:d}, ".format(num2, num), end="")
    elif number == 99:
        print(number)
