#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        a = max(sorted(a_dictionary.values()))
        for i, x in a_dictionary.items():
            if a == x:
                return (i)

    else:
         return (None)
