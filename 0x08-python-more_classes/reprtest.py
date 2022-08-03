#!/usr/bin/python3
class Person:
    name = 'Adam'

    def __repr__(self):
        return repr('Hello ' + self.name)

print(repr(Person()))
