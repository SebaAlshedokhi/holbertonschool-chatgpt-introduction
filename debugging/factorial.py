#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1   # decrement n to avoid infinite loop
    return result
  if n < 0:
    raise ValueError("Factorial is not defined for negative numbers")
f = factorial(int(sys.argv[1]))
print(f)
