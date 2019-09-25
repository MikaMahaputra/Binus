# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 11:46:58 2019

@author: user
"""

import string
def ignore_punctuation(word):
    return "",join(letter.lower()for letter in word if letter in string.ascii_letters)
def reverse(word):
    return word[::-1]
def is_palindrome(word):
    word = ignore_punctuation(word)
    rev= reverse(word)
    if (word == rev):
        return True
    else:
        return False
    
word= str(input("Enter a word"))
result= is_palindrome(word)

if result:
    print("Yes, it's a palindrome")
else:
    print("It's not a palindrome")
