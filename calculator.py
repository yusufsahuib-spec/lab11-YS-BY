"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
#check for cdfghj
import math

# First example
def add(a, b): 
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    if a==0:
        raise ZeroDivisionError("Zero Division Error")
    return b/a

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