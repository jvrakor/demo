import sys
import os

def greet(name):
    print("Hello, " + name + "!")

def add(a,b):
    return a+b

def main():
    greet("World")
    result = add(2,3)
    print("2 + 3 =", result)

if __name__ == "__main__":
    main()
