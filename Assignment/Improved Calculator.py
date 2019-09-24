# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 10:44:27 2019

@author: user
"""
print ("Welcome")
choice= input("What would you like to do? (Press 1 for Addition, Press 2 for Substraction, Press 3 for Multiplication, Press 4 for Division ")
if(choice=="1"):
    firstnum1= input ("Enter Your First Number: ")
    secnum1 = input ("Enter Your Second Number : ")
    def addition(firstnum1, secnum1):
      return int(firstnum1) + int(secnum1)
    print ("The Answer Is: ",addition(firstnum1, secnum1))

elif(choice=="2"):
    firstnum2= input ("Enter Your First Number: ")
    secnum2 = input ("Enter Your Second Number : ")
    def substraction(firstnum2, secnum2):
      return int(firstnum2) - int(secnum2)
    print ("The Answer Is: ",substraction(firstnum2, secnum2))

elif(choice=="3"):
    firstnum3= input ("Enter Your First Number: ")
    secnum3 = input ("Enter Your Second Number : ")
    def multiplication(firstnum3, secnum3):
      return int(firstnum3) * int(secnum3)
    print ("The Answer Is: ",multiplication(firstnum3, secnum3))    
    
elif(choice=="4"):
    firstnum4= input ("Enter Your First Number: ")
    secnum4 = input ("Enter Your Second Number : ")
    def division(firstnum4, secnum4):
      return int(firstnum4) // int(secnum4)
    print ("The Answer Is: ",division(firstnum4, secnum4))
    
else:
    print("Error please try again")