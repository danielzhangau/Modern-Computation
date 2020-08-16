# -*- coding: utf-8 -*-
"""
Factorial function as a recursive function

Consult: https://en.wikipedia.org/wiki/Factorial

Created on Fri Feb  1 11:41:38 2019

@author: shakes
"""

def factorial(n):
    '''
    Factorial function with recursion
    '''
    
    #base case
    if n == 1:
        return 1
    if n == 2:
        return n * factorial(n-1)
    if n == 3:
        return n * factorial(n-1)
    #recursive call
    else:
        return n * factorial(n-1)
        #multiply


print("5!:", factorial(5)) #should be 120
print("10!:", factorial(10)) #should be 3628800
