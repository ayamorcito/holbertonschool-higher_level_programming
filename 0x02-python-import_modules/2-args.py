#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    num = len(sys.argv)

    if num == 1:
        print(f"{(num - 1)} arguments.")

    else:
        print(f"{num} arguments:")
    
    for i in range(1, num):
        print(f"{i}: {sys.argv[i]}")
