print ("Hello my name is Steve Harvey and welcome to Family Feud!\nThis game will be played by 2 players\nYou will be given a list of questions, and you will have to answer accordingly\nGood luck!")

point1a= 0
point2a= 0
point3a= 0
point4a= 0
point5a= 0
totala= point1a+point2a+point3a+point4a+point5a

point1b= 0
point2b= 0
point3b= 0
point4b= 0
point5b= 0
totalb= point1b+point2b+point3b+point4b+point5b


def question_1a():
    answer1a= input("Who was the most popular character on the sitcom Friends? ")
    point1a = 0
    if answer1a == "rachel":
        point1a = 19
        print ("You have earned 19 points!")
    elif answer1a == "joey":
        point1a = 17
        print ("You have earned 17 points!")
    elif answer1a == "ross":
        point1a = 16
        print ("You have earned 16 points!")
    elif answer1a == "chandler":
        point1a = 16
        print ("You have earned 16 points!")
    elif answer1a == "monica":
        point1a = 14
        print ("You have earned 14 points!")
    elif answer1a == "phoebe":
        point1a = 10
        print ("You have earned 10 points!")
    else:
        print ("You have earned 0 points!")
question_1a()

def question_2a():
    answer2a = input ("Name a material medals are made of ")
    point2a = 0
    
    if answer2a == "gold":
        point2a += 29
        print ("You have earned 29 points!")
    elif answer2a == "silver":
        point2a += 25
        print("You have earned 25 points!")
    elif answer2a == "bronze":
        point2a += 20
        print ("You have earned 20 points!")
    else:
        print ("You have earned 0 points!")
question_2a()

def question_3a():
    answer3a = input("A doctor has many things, what is it ?")
    if answer3a == "patient":
        point3a = 40
        print ("You have earned 40 points!")
    elif answer3a == "instrument":
        point3a = 28
        print ("You have earned 28 points!")
    elif answer3a == "knowledge":
        point3a = 25
        print ("You have earned 25 points!")
    elif answer3a == "medicine":
        point3a = 18
        print ("You have earned 18 points!")
    else:
        print("You have earned 0 points!")
question_3a()

def question_4a():
    answer4a= input("On a scale on 1-5 how cool is Binus? ")
    if answer4a == "1":
        point4a= 7
        print ("You've earned 7 points!")
    elif answer4a == "2":
        point4a= 14
        print ("You've earned 14 points!")
    elif answer4a == "3":
        point4a= 21
        print ("You've earned 21 points!")
    elif answer4a == "4":
        point4a= 28
        print ("You've earned 28 points!")
    elif answer4a == "4":
        point4a= 35
        print ("You've earned 35 points!")
    else:
        print ("You've earned 0 points!")
question_4a()

def question_5a():
    answer5a= input("What ride should a person avoid if he/she is panicking")
    if answer5a == "rollercoaster":
        point5a = 50
        print ("You have earned 50 points!")
    elif answer5a == "airplane":
        point5a = 36
        print ("You have earned 36 points!")
    elif answer5a == "motorcycle":
        point5a = 18
        print ("You have earned 18 points!")
    elif answer5a == "car":
        point5a = 10
        print ("You have earned 10 points!")
    else:
        print("You have earned 0 points!")
print ("You have earned: ", totala)
question_5a()
        
def question_1b():
    answer1b= input("Who was the most popular character on the sitcom Friends? ")
    point1b = 0
    if answer1b==answer1a:
        print("You've earned 0 points!")
    elif answer1b == "rachel":
        point1b = 19
        print ("You have earned 19 points!")
    elif answer1b == "joey":
        point1b = 17
        print ("You have earned 17 points!")
    elif answer1b == "ross":
        point1b = 16
        print ("You have earned 16 points!")
    elif answer1b == "chandler":
        point1b = 16
        print ("You have earned 16 points!")
    elif answer1b == "monica":
        point1b = 14
        print ("You have earned 14 points!")
    elif answer1b == "phoebe":
        point1b = 10
        print ("You have earned 10 points!")
    else:
        print ("You have earned 0 points!")    
        
question_1b

def question_2b():
    answer2b = input ("Name a material medals are made of ")
    point2b = 0
    
    if answer2b == answer2a:
        print("You have earned 0 points!")
    elif answer2b == "gold":
        point2b += 29
        print ("You have earned 29 points!")
    elif answer2b == "silver":
        point2b += 25
        print("You have earned 25 points!")
    elif answer2b == "bronze":
        point2b += 20
        print ("You have earned 20 points!")
    else:
        print ("You have earned 0 points!")
question_2b()
    
def question_3b():
    answer3b = input("A doctor has many things, what is it ?")
    if answer3b == answer3a:
        print("You have earned 0 points!")
    elif answer3b == "patient":
        point3b = 40
        print ("You have earned 40 points!")
    elif answer3b == "instrument":
        point3b = 28
        print ("You have earned 28 points!")
    elif answer3b == "knowledge":
        point3b = 25
        print ("You have earned 25 points!")
    elif answer3b == "medicine":
        point3b = 18
        print ("You have earned 18 points!")
    else:
        print("You have earned 0 points!")
question_3b()

def question_4b():
    answer4b= input("On a scale on 1-5 how cool is Binus? ")
    if answer4b == answer4a:
        print("You have earned 0 points!")
    elif answer4b == "1":
        point4b= 7
        print ("You've earned 7 points!")
    elif answer4b == "2":
        point4b= 14
        print ("You've earned 14 points!")
    elif answer4b == "3":
        point4b= 21
        print ("You've earned 21 points!")
    elif answer4b == "4":
        point4b= 28
        print ("You've earned 28 points!")
    elif answer4b == "4":
        point4b= 35
        print ("You've earned 35 points!")
    else:
        print ("You've earned 0 points!")
question_4b()   

def question_5b():
    answer5b= input("What ride should a person avoid if he/she is panicking")
    if answer5b == answer5a:
        print ("You have earned 0 points!")
    elif answer5b == "rollercoaster":
        point5b = 50
        print ("You have earned 50 points!")
    elif answer5b == "airplane":
        point5b = 36
        print ("You have earned 36 points!")
    elif answer5b == "motorcycle":
        point5b = 18
        print ("You have earned 18 points!")
    elif answer5b == "car":
        point5b = 10
        print ("You have earned 10 points!")
    else:
        print("You have earned 0 points!")
print ("You have earned: ", totala)
question_5b()
    
totalpoints= totala + totalb
def final():
    print ("You have accumulated a total of ", totalpoints, "so far")
    if totalpoints >200:
        print ("Congratulations, you have won the game!")
    elif totalpoints == 200:
        print ("Congratulations, you have won the game!")
    else:
        print ("It looks like you dont have enough points good luck next time!")

      
    