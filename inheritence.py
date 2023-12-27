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

class Employee:
    company = "Visa"
    eCode = 120


class Freelancer:
    company = "Fiverr"
    level = 2

    def upgradeLevel(self):
        self.level = self.level + 1


class Programmer(Employee, Freelancer):
    name ="Rohit"

p = Programmer()
p.upgradeLevel()
print(p.level)