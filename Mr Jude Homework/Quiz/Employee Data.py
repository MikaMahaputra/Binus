#This is a pre-alpha build
#Build 0.1337

import re


class Menu:
    def __init__(self, data):
        self.data = data
        self.mainmenu()

    def mainmenu(self):
        print("1. New Staff")
        print("2. Delete Staff")
        print("3. View Summary Data")
        print("4. Save & Exit")

    def choose(self, option):
        while True:
            if option == 1:
                self.add_staff()
            elif option == 2:
                self.remove_staff()
            elif option == 3:
                self.view_data()
            elif option == 4:
                self.save()
                break
            else:
                print("Choose a valid option")
            option = int(input("Input Choice: "))

    def add_staff(self):
        print("New Staff")
        staff = Staff(self.data)
        self.data.append(f"{staff.id}#{staff.name}#{staff.position}#{staff.salary}\n")

    def remove_staff(self):
        while True:
            id = input("Input ID[SXXXX]:")
            if not re.match(r"S[0-9]{4}", id):
                continue
            break
        staff_exists = len([row for row in self.data if row[:5] == id])
        if staff_exists:
            self.data = [row for row in self.data if row[:5] != id]
            print("Data has been successfully deleted")
        else:
            print("Data Not Found")

    def view_data(self):
        split_data = [row.split("#") for row in self.data]
        staff_salaries = [int(row[3]) for row in split_data if row[2] == "Staff"]
        officer_salaries = [int(row[3]) for row in split_data if row[2] == "Officer"]
        manager_salaries = [int(row[3]) for row in split_data if row[2] == "Manager"]

        if len(staff_salaries):
            max_staff_salary = max(staff_salaries)
            min_staff_salary = min(staff_salaries)
            average_staff_salary = sum(staff_salaries) / len(staff_salaries)
        else:
            max_staff_salary = 7000000
            min_staff_salary = 3500000
            average_staff_salary = 525000

        if len(officer_salaries):
            max_officer_salary = max(officer_salaries)
            min_officer_salary = min(officer_salaries)
            average_officer_salary = sum(officer_salaries) / len(officer_salaries)
        else:
            max_officer_salary = 10000000
            min_officer_salary = 7000001
            average_officer_salary = 8500000

        if len(manager_salaries):
            max_manager_salary = max(manager_salaries)
            min_manager_salary = min(manager_salaries)
            average_manager_salary = sum(manager_salaries) / len(manager_salaries)
        else:
            max_manager_salary = 0
            min_manager_salary = 10000001
            average_manager_salary = 0

        print("1. Staff")
        print(f"Minimum Salary: {min_staff_salary}")
        print(f"Maximum Salary: {max_staff_salary}")
        print(f"Average Salary: {average_staff_salary}\n")

        print("2. Officer")
        print(f"Minimum Salary: {min_officer_salary}")
        print(f"Maximum Salary: {max_officer_salary}")
        print(f"Average Salary: {average_officer_salary}\n")

        print("3. Manager")
        print(f"Minimum Salary: {min_manager_salary}")
        print(f"Maximum Salary: {max_manager_salary}")
        print(f"Average Salary: {average_manager_salary}\n")

    def save(self):
        with open("data.txt", "w") as f:
            for row in self.data:
                f.write(row)
            f.close()


class Staff:
    def __init__(self, data):
        self.id = ""
        self.name = ""
        self.position = ""
        self.salary = "0"
        self.position_data = {
            "Staff": ["3500000", "7000000"],
            "Officer": ["7000001", "10000000"],
            "Manager": ["10000001"],
        }
        self.existing_ids = [row.split("#")[0] for row in data]

        self.enter_initial_data()

    def enter_initial_data(self):
        while True:
            self.id = input("Input ID[SXXXX]:")
            if not re.match(r"S[0-9]{4}", self.id) or self.id in self.existing_ids:
                continue
            break
        while True:
            self.name = input("Input Name[0...20]:")
            if len(self.name) == 0 or len(self.name) > 20:
                continue
            break
        while True:
            self.position = input("Input Position[Staff|Officer|Manager]:")
            if self.position not in self.position_data:
                continue
            break
        if self.position == "Manager":
            while True:
                self.salary = input(f"Input salary for {self.position}:")
                if int(self.salary) < int(self.position_data[self.position][0]):
                    continue
                break
        else:
            while True:
                self.salary = input(f"Input Salary for {self.position}:")
                if int(self.salary) < int(self.position_data[self.position][0]) or int(
                    self.salary
                ) > int(self.position_data[self.position][1]):
                    continue
                break


def main():
    with open("data.txt", "r") as f:
        rows = f.readlines()
        print('|ID\t\t|Name\t\t|Position\t\t|Salary\t\t|')
        for row in rows:
          row = row.strip().split('#')
          print(f'|{row[0]}\t\t|{row[1]}\t\t|{row[2]}\t\t|{row[3]}\t\t|')
        print('\n')
        menu = Menu(rows)
        choice = input("Input Choice: ")
        menu.choose(int(choice))


main()
       
