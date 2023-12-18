# def large(x,y,z):
#     l = x
#     if (y>l):
#         l = y
#     if (z>l):
#         l = z
#     return l
# b = int(input("Enter any number: "))
# c = int(input("Enter any number: "))
# d = int(input("Enter any number: "))
# a = large(b,c,d)
# print(a)

# def celtofer(x):
#     a =( x * (9/5)) + 32
#     return a
# y = int(input("Enter the temperture in degree celcius: "))
# z = celtofer(y)
# print(z)

# def addrecur(n):
#     if n == 1:
#         return 1
#     return n+addrecur(n-1)

# x = int(input("Enter any number: "))
# s = addrecur(x)
# print(s)

def remove_and_strip(string, word):
    newstr = string.replace(word, "")
    return newstr
x = input("Enter your string: ")
n = remove_and_strip(x,y)
print(n)