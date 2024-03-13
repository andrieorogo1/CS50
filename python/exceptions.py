import sys # A module to exit a program

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: Invalid input.")
    sys.exit(1)

try: 
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    sys.exit(1)

"""

To avoid not having a messy error like this use exception handling.

Traceback (most recent call last):
  File "/Users/andrie/Documents/cs50/python/lambda.py", line 7, in <module>
    people.sort()
TypeError: '<' not supported between instances of 'dict' and 'dict'

"""
print(f"{x} / {y} = {result}")