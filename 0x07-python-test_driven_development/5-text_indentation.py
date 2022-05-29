#!/usr/bin/python
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")


    p = 0
    while p < len(text) and text[p] == ' ':
        p += 1


    while p < len(text):
       print(text[p], end="")
       if text[p] in ".?:":
           print("\n")

           p += 1
           while p < len(text) and text[p] == ' ':
              p += 1
           continue
       p += 1
        
