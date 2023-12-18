# 1

# a = int(input("Enter any number: "))
# b = int(input("Enter any number: "))
# c = int(input("Enter any number: "))
# d = int(input("Enter any number: "))

# max_number = a  # Assume a is the maximum initially

# if b > max_number:
#     max_number = b

# if c > max_number:
#     max_number = c

# if d > max_number:
#     max_number = d

# print("The maximum number is:", max_number)

# 2

# Physics = int(input("Enter marks in physics: "))
# Chemistry = int(input("Enter marks in Chemistry: "))
# Maths = int(input("Enter marks in Maths: "))
# x = (Physics/100)*100
# y = (Chemistry/100)*100
# z = (Maths/100)*100
# s = ((Physics+Chemistry+Maths)/3)
# if x>33 and y>33 and z>33 and s>40:
#     print("Pass")
# else:
#     print("Fail")

# 3
#  
# text = input("Enter the text: ")

# if ("make a lot of money" in text):
#     spam = True
# elif ("buy now" in text):
#     spam = True
# elif ("click this" in text):
#     spam = True
# elif ("subscribe this" in text):
#     spam = True
# else:
#     spam = False

# if (spam):
#     print("This text is spam")
# else:
#     print("This text is not spam")

# 4

# x = input("Enter your username: ")
# y = len(x)
# if y>10:
#     print("Username contains less than 10 Characters")
# else:
#     print("Username contains more than 10 Characters")

# 5

# l_o_n = ["harry", "ram", "rohit", "mohit", "neha", "radha", "modi"]
# name = input("Enter the name: ")
# if name in l_o_n:
#     print("Your name is in the list")
# else:
#     print("Your name is not in the list")

# 6

x = int(input("Enter your marks: "))
if x>90 and x<100:
    y = "Ex"
elif x>80 and x<90:
    y = "A"
elif x>70 and x<80:
    y = "B"
elif x>60 and x<70:
    y = "C"
elif x>50 and x<60:
    y = "D"
else:
    y = "F"
print("Your grade is "+y)