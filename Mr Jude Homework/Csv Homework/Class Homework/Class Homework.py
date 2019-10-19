class Account():
    balance= 0
    
    def __init__(self,balance2):
        self.balance= balance2
    
    def getBalance(self):
        return self.balance
    
    def deposit(self,amt):
        if amt > 0:
            self.balance = self.balance + amt
            return True
        else:
            return False
        
    def withdraw(self,amt):
        if (self.balance > amt):
            self.balance = self.balance - amt
            return True
        else:
            return False
        
myAccount = Account(5000)

if (myAccount.deposit(10000)):
    print("Account balance is >>",myAccount.getBalance())
    
class Customer():
    firstName= ""
    lastName= ""
    account= Account(5000)
    
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        
    def getFirstName(self):
        return self.firstName
    
    def getLastName(self):
        return self.lastName
    
    def getAccount(self):
        return self.account
    
    def setAccount (self, otherAccount):
        self.account = otherAccount
        
firstCustomer = Customer("Erwin", "Rommel")
print (firstCustomer.getFirstName(), firstCustomer.getLastName()) 

class Bank():
    customers = []
    numberOfCustomers = 0
    bankName= ""
    
    def __init__(self, bankName):
        self.bankName = bankName
        
    def AddCustomer(self, firstName, lastName):
        self.customers.append(Customer(firstName, lastName))
        self.numberOfCustomers = self.numberOfCustomers + 1
        
    def GetNumOfCustomers(self):
        return self.numberOfCustomers
    
    def GetCustomer(self, index):
        return self.customers(index)

firstBank= Bank("Big Bang")
print ("The current Customer is: ",firstBank. GetNumOfCustomers())
firstBank.AddCustomer("Erwin", "Rommel")
print ("Status updated")
print ("The current Customer is: ",firstBank.GetNumOfCustomers())
    

       
        