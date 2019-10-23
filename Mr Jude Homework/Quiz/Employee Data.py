#This is a pre-alpha build
#Build 0.1337

filename = "data.txt"

def Menu():
    print ("Welcome To Criminal Bro's Database")
    print ("Press 1 To Add New Staff")
    print ("Press 2 To Delete A Staff")
    print ("Press 3 To View All Privates Data :D")
    print ("Press 4 To Save & Exit")
    print ("Pressing Any Other Button Will Initiate Self Destruct")
    choice = input ("Please Choose An Option ")
    if (choice == "1"): 



class Employee:
    def __init__(self, staffid, name, position, salary):
        self.staffid = staffid
        self.name = name
        self.salary = salary
        self.position = position
        self.salary = salary
    
    def displaystaff(self):
        print ("ID: ", self.staffid, "Name : ", self.name, "Position: ", self.position, "Salary: ", self.salary)

emp1 = Employee("S1337", "Erwin Test", "Officer", "50.000")   
emp1.displaystaff()     

