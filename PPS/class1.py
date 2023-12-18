# WAP to add the digits of the number given by the user
x = int (input("Enter any number: "))
c = 0
while (x>0):
    y=x%10
    c = c+y
    x = x//10
print(c)

# WAP to find the sum of n natural numbers n input by user
a = int(input("Enter any number: "))
b = 0
for i in range (1,a+1):
    b += i
print(b)