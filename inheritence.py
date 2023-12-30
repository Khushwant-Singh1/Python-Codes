# class Employee:
#     company = "Google"
#
#     def showDetails(self):
#         print("This is an employee")
#
# class Programmer(Employee):
#     language = "Python"
#     # company = "Youtube"
#
#     def getLanguage(self):
#         print(f"The language is {self.language}")
#     def showDetails(self):
#         print("This is an programmer")
#
# e = Employee()
# e.showDetails()
# p = Programmer()
# p.showDetails()
# print(p.company)

# class Employee:
#     company = "Visa"
#     eCode = 120
#
#
# class Freelancer:
#     company = "Fiverr"
#     level = 2
#
#     def upgradeLevel(self):
#         self.level = self.level + 1
#
#
# class Programmer(Employee, Freelancer):
#     name ="Rohit"
#
# p = Programmer()
# p.upgradeLevel()
# print(p.level)
#
# class Person:
#     country = "India"
#
#     def __init__(self):
#         print("Initializing Person...\n")
#     def  takeBreath(self):
#         print("I am breathing...")
#
# class Employee(Person):
#     company = "Honda"
#
#     def __init__(self):
#         super().__init__()
#         print("Initializing Employee...\n")
#
#     def getSalary(self):
#         super().takeBreath()
#         print(f"I am an Employee so I am luckily breathing...")
#
# class Programmer(Employee):
#     company = "Fiverr"
#
#     def __init__(self):
#         super().__init__()
#         print("Initializing Programmer...\n ")
#
#     def getSalary(self):
#         print(f"No salary to programmer")
#
#     def takeBreath(self):
#         super().takeBreath()
#         print("I am a programmer so I am breathing++...")
#
#
# p = Person()
# p.takeBreath()
# e = Employee()
# e.takeBreath()
# pr = Programmer()
# pr.takeBreath()
#
# class Employees:
#     company = "Camel"
#     salary  = 100
#     location = "Delhi"
#
#     def changeSalary(self, sal):
#          self.__class__.salary = sal
#
#     @classmethod
#     def changeSalary(cls, sal):
#         cls.salary = sal
#
# e = Employees()
# print(e.salary)
# e.changeSalary(455)
# print(e.salary)
# print(Employees.salary)

class Employee:
    company = "Bharat Gas"
    salary = 5600
    salarybonus = 400
    # totalSalary = 6000

    @property
    def totalSalary(self):
        return self.salary + self.salarybonus

    @totalSalary.setter
    def totalSalary(self, val):
        self.salarybonus = val - self.salary

e = Employee()
print(e.totalSalary)
e.totalSalary = 5800
print(e.salary)
print(e.salarybonus)

class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, num2):
        print("Let's add")
        return self.num + num2.num

    def __mul__(self, num2):
        print("Let's multiply")
        return self.num * num2.num

    def __str__(self):
        return f"Decimal Number: {self.num}"

    def __len__(self):
        return 1

# n1 = Number(4)
# n2 = Number(6)
# sum = n1 + n2
# mul = n1 * n2
# print(sum)
n = Number(9)
print(n)