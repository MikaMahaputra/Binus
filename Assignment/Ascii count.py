# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 22:52:12 2019

@author: user
"""
def countletter(str_input):
    a= []
    b= []
    for i in str_input:
        if i not in a:
            a.append(i)
            b.append(1)
        else:
            x=findinlist(i,a)
            b[x]+=1
    for i in range(len(a)):
        print(a[i], "=", b[i])
