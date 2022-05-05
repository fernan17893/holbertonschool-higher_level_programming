
#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    words = dir(hidden_4)
    for j in words:
        if j[0] != '_' and j[1] != '_':
            print("{}".format(j))
