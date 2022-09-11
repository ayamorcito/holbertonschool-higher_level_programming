#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    argc = len(argv[1:])
    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print(f"1 argument:\n{argc}: {argv[1]}")
    else:
        print(f"{argc} arguments:")
        for i in range(argc):
            print(f"{i + 1}: {argv[i + 1]}")
