import math
# class Programmer:
#     company = "Microsoft"
#
#     def __init__(self, name, product):
#         self.name = name
#         self.product = product
#
#     def getInfo(self):
#         print(f"The name of the {self.company} programmer is {self.name} and the product is {self.product}")
#
# harry = Programmer("Harry", "Skype")
# alka = Programmer("Alka", "GitHub")
# harry.getInfo()
# alka.getInfo()


# class Calculator:
#
#     def __init__(self, num):
#         self.number = num
#
#     def square(self):
#
#         return self.number*self.number
#
#     def cube(self):
#
#         return self.number * self.number*self.number
#
#     def root(self):
#         return math.sqrt(self.number)
#      @staticmethod
#      def greet():
#          print("Hello")

#
# x = int(input("Enter"))
# num = Calculator(x)
# num.greet()
# print(num.cube())
# print(num.root())
# print(num.square())

# class Sample:
#     a = "Harry"
# obj = Sample()
# obj.a = "Vikky"
# # Sample.a = "Vikky"
# print(Sample.a)
# print(obj.a)

class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats
    def getStatus(self):
        print("***********************")
        print(f"The name of the train is {self.name}")
        print(f"The fare of the train is {self.fare}")
        print(f"The seats of the train is {self.seats}")
        print("************************")

    def fareInfo(self):
        print(f"The price of the ticket is : {self.fare}")

    def bookTicket(self):
        if (self.seats>0):
            print(f"your tickets has been booked! your seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("sorry!")

    def cancelTicket(self):
        pass




intercity = Train("Intercity Express: 14015", 90, 300)
intercity.getStatus()
intercity.fareInfo()
intercity.bookTicket()
intercity.getStatus()

