# Create a Rectangle class with attributes length and width. Include methods to calculate the area and perimeter of the rectangle.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

    def perimeter(self):
       return 2 * (self.length + self.width)

r = Rectangle(8, 10)
print("The area of rectangle is: ", r.area())
print("The perimeter of rectangle is: ", r.perimeter())

#Implement a Student class with attributes name, age, and grade. Include a method to display the student's information.

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    def info(self):
        print(f"The name of student is {self.name}, age of student is {self.age}, grade of student is {self.grade}")

st = Student("Khushwant Singh", 17, 84)
st.info()

# Create a BankAccount class with attributes account_number, account_holder, and balance. Include methods to deposit and withdraw funds from the account.

class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, funds):
        self.balance += funds

    def withdraw(self, funds):
        self.balance -= funds

    def info(self):
        print(f"Name of account holder is {self.account_holder}, account number of {self.account_number} and balance of account is {self.balance}")


a = BankAccount(1843559464,"Khushwant Ambani",1000000000000000000000000)
a.info()
a.deposit(1000000)
a.info()
a.withdraw(500000)
a.info()
# Implement a Circle class with attribute radius. Include methods to calculate the area and circumference of the circle.
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi*self.radius*self.radius

    def circumference(self):
        return 2*math.pi*self.radius

ci = Circle(9)
print("The area of circle is ", ci.area())
print("The circumference is ", ci.circumference())

# Create a Person class with attributes name and age. Implement a method to check if the person is eligible to vote (age >= 18).

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def check(self):
        if self.age >= 18:
            return "Eligible"
        else:
            return "Not Eligible"
pe = Person("Khushwant Singh", 17)
print(pe.check())

# Design a Book class with attributes title, author, and price. Include a method to display the book's details.

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def info(self):
        print(f"The title of book is {self.title} its author's name {self.author} and its prize ₹{self.price}")

rich = Book("Rich Dad Poor Dad", "Robert Kiyosaki",322)
rich.info()

# Implement a Car class with attributes make, model, and year. Include methods to start the car, stop the car, and display its details.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.running = False

    def start(self):
        if not self.running:
            print("Starting the car...")
            self.running = True
        else:
            print("car is running.")

    def stop(self):
        if self.running:
            print("Stopping the car...")
            self.running = False
        else:
            print("The car has stopped")

    def details(self):
        print(f"Car Details: Make - {self.make}, Model - {self.model}, Year - {self.year}, Running - {self.running}")

my_car = Car("Lamborghini", "Revuelto", 2023)
my_car.start()
my_car.details()
my_car.stop()
my_car.details()

# Create a Calculator class with methods for addition, subtraction, multiplication, and division.

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        return self.num1 + self.num2
    def subtraction(self):
        return self.num1 - self.num2

    def multiplication(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num1 / self.num2


cal = Calculator(8,4)
print("The result of addition is: ", cal.addition())
print("The result of subtraction is: ", cal.subtraction())
print("The result of multiplication is: ", cal.multiplication())
print("The result of divide is: ", cal.divide())


# Design a Bank class that manages multiple BankAccount objects. Include methods to add a new account, display all accounts, and calculate the total balance.

class Bank:
    pass


# Implement a Rectangle class with attributes length and width. Add a method to compare two rectangles based on their area.