#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lastdigit = -(-number % 10)
else:
    lastdigit = number % 10
if lastdigit > 5:
    strn = "and is greater than 5"
elif lastdigit <= 5 and lastdigit != 0:
    strn = "and is less than 6 and not 0"
else:
    strn = "and is 0"
print(f"Last digit of {number} is {lastdigit} {strn}")
