# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 22:46:00 2019

@author: user
"""

str1 = input(("Input Your First Word "))
str2 = input(("Input Your Second Word "))
def check_anagram(str1, str2):
    if (sorted(str1) == sorted(str2)):
        print ("The strings are anagrams")
    else:
        print ("The strings aren't anagrams")
check_anagram(str1,str2)   