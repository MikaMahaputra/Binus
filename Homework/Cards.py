#%%
import random
def printCard():
    x = []
    shapes = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
    numbers = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    for a_shapes in shapes:
        for a_numbers in numbers:
            x.append(a_shapes + ' ' + a_numbers)
            random.shuffle(x)
    for i in x:
        print(i)
printCard()

#Made By Almada Putra and Mika Mahaputra