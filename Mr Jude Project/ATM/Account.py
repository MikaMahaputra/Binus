
class Account():
    balance= 0
    pin= 0
    bankNumber= 0
    
    def __init__(self, balance, pin, bankNumber):
        self.balance= balance
        self.pin = pin
        self.bankNumber= bankNumber
#Function For Getting Balance    
    def getBalance(self):
        return self.balance
#Function For Getting PIN          
    def getPin(self):
        return self.pin
#Function For Getting Bank Number       
    def getBankNumber(self):
        return self.bankNumber
#Function To Update Balance    
    def setBalance(self, balance):
        self.balance = balance
        return self.balance


    