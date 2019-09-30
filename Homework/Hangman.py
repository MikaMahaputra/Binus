# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 11:46:58 2019

@author: user
"""
import random

def get_word() :
    words= ["Happy", "Sad", "Angry", "Dog", "Cat", "Mouse", "Air", "Land", "Sea", "January", "May", "June", "December"]
    return random.choice(words).upper()
def check (word, guesses, guess):
    guess= guess.upper
    status= ""
    matches= 0
    for letter in word:
        if letter in guesses:
            status += letter
        else:
            status += "*"
        if letter == guess:
            matches += 1
    if matches == 1:
        print("Yes, this word contains the letter", + guess)
    else:
        print ("Sorry, the word does not contain this letter")
        
    return status
    
def main ():
    word = get_word()
    guesses = []
    guessed = False
    print ("The word contains", len(word), "letters")
    while not guessed:
        text = ("Please enter one letter: " , len(word))
        guess = input (text)
        guess = guess.upper()
        if guess in guesses:
            print ("You've already guessed that letter")
        elif len(guess) == 1 :
            guesses.append (guess)
            result = check(word,guesses,guess)
            if result == word:
                guessed = True
            else: 
                print(result)
        else:
            print("Error, please try again")
    print("Yes the word is",word )
 
main ()               
        
#Made By Almada Putra and Mika Mahaputra
