"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
#check for cdfghj

#https://github.com/yusufsahuib-spec/lab11-YS-BY/blob/main/calculator.py
# First example
import math

def square_root(a):
    try:
        if a<0:
            raise ValueError("Integrand cannot be a negative number")
        return math.sqrt(a)
    except ValueError:
        raise ValueError("Integrand cannot be a negative number")


def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b): 
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    if a==0:
        raise ZeroDivisionError
    return a/b

def logarithm(a, b):
    if a <=0:
        raise ValueError("Base cannot be negative")
    if a==1:
        raise ValueError("One raised to anything is one")
    if b<=0:
        raise ValueError("Argument must be a positive number")
    return math.log(b,a)

def exponent(a,b):
    return a**b