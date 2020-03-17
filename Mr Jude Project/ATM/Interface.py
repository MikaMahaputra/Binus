#Importing preivous files
import Account
import Atm
from pygame import mixer

def music():
    mixer.init()
    mixer.music.load("wii.mp3")
    mixer.music.play(loops=-1)

def nope():
    mixer.music.stop()    
    mixer.music.load("nope.mp3")
    mixer.music.play()
    
#Call To Play The Music    
music()

#Variables In Account Class
bankNumber= int(input("Please enter your bank number: "))
pin = int(input("Please enter your PIN: "))
balance= int(input("Please enter your balance: "))

myAccount= Account.Account(balance, pin, bankNumber)

#Variables In Atm Class
bankName= (input("Please enter your bank name: "))
atmLocation= (input("Please enter your atm location: "))
myAtm = Atm.ATM(bankName,atmLocation)

#Variables for interface
inputPin= 0
inputChoice= 0
ammountTaken= 0
accountTransfer = 0
ammountTransfer = 0
checkLoop = True
checkLoop2 = True

#Function To Confirm An Action

def ConfirmationMenu():
    print("Do You Want To Do Another Transaction ?")
    print("1. Yes")
    print("2. No")
    inputChoice= int(input("Please Choose An Option\n "))
    if (inputChoice == 1):
        print("\033[H\033[J")
        return True
    elif(inputChoice ==2):
        print ("\033[H\033[J")
        print("Thank You For Using This ATM")
        nope()
        return False       
    
    

print("\033[H\033[J") #Used To Clear Console
print("Welcome To", myAtm.getbankName())

while checkLoop2:
    inputPin= int(input("Please Enter Your Pin\n"))
    if(myAtm.CheckPin(inputPin,myAccount.getPin()) == True):
        while (checkLoop):
            ("\033[H\033[J")
            print("1. Check Balance")
            print("2. Withdraw Money")
            print("3. Transfer")
            print("4. Exit")
            inputChoice = int(input("Please Select An Option "))
            if(inputChoice == 1):
                print("\033[H\033[J")
                print("Your Current Balance Is\n", myAtm.CheckBalance(myAccount.getBalance()))
                checkLoop = ConfirmationMenu()
                checkLoop2= checkLoop
            elif(inputChoice == 2):
                print("\033[H\033[J")
                ammountTaken = int(input("Please Enter The Amount To Withdraw \n"))
                if(myAtm.Withdraw(myAccount.getBalance(), ammountTaken) == True):
                    myAccount.setBalance(myAtm.SetNewBalance(myAccount.getBalance(), ammountTaken))
                    print("Withdrawal Successfull")            
                else:
                    print("Insufficient Balance")
                checkLoop = ConfirmationMenu()
                checkLoop2= checkLoop
                
            elif(inputChoice == 3):
                print("\033[H\033[J")
                accountTransfer= int(input("Please Enter An Account Number \n"))
                ammountTransfer= int(input("Please Enter How Much To Transfer \n"))
                if(myAtm.Transfer(myAccount.getBalance(), accountTransfer, ammountTransfer) == True):
                    myAccount.setBalance(myAtm.SetNewBalance(myAccount.getBalance(), ammountTransfer))
                    print("Transfer Successfull")
                else:
                    print("Please Check Your Transaction Again")
                    checkloop = ConfirmationMenu()
                    checkLoop2= checkLoop
                checkloop = ConfirmationMenu()
                checkLoop2= checkLoop
            elif(inputChoice == 4):
                print ("\033[H\033[J")
                print ("Thank You For Using This ATM")
                nope()
                checkLoop = False
                checkLoop2 = False
            
            
    else:
        print("\033[H\033[J")
        print("Invalid PIN ")
        


