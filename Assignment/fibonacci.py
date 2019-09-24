# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 22:52:12 2019

@author: user
"""
n= int(input(("Input a number ")))
def fibonacci(n):
    if n<0:
        print("Error please try again")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
(fibonacci(n))