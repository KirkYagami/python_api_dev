"""
This module is for basic math operations
"""



def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def division(a,b):
    return a/b

def floor_division(a,b):
    return a//b

def square(num):
    return num*num

def mod(a,b):
    return a%b

# print(" This will be executed always")


if __name__=="__main__":
    print("this is will be executed only when we are running this module directly")
    print(add(3,4))

