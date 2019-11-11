#Class For ATM


class ATM:    
    bankName = "Big Bang"
    atmLocation = "Kemang"

    
    def __init__(self,bankName,atmLocation):
        self.bankName = bankName
        self.atmLocation = atmLocation
        
    def getbankName(self):
        return self.bankName
#To make sure the inputted pin is correct    
    def CheckPin(self,pinInput, pinAccount):
        if (pinInput == pinAccount):
            return True
        else:
            return False
#Checking Balance as usual    
    def CheckBalance(self, balance):
        return balance
    
#To check and only function when user withdraws any ammount bigger than zero
#And to make sure the balance is enough to be deducted                
    def Withdraw(self, balance, ammount):
        if (ammount > 0):
            if (balance > ammount):
                return True
            else:
                return False
        else:
            return False
#To make sure to transfer to a valid account
#And to make sure the balance is enough to be deducted
    def Transfer(self,balance, bankAccount, ammount):
        if (len(str(bankAccount) )== 12):
            if (balance > ammount):                
                return True
            else:
                return False
        else:
            return False
#Function To Deduct Balance                
    def SetNewBalance(self,balance,ammount):
        return balance - ammount