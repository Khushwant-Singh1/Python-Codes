# x = []
# y = int(input("Enter any number: "))
# for i in range (y):
#     z = int(input("enter any number: "))
#     x.append(z)
# x.reverse()
# print(x)

x = []
y = int(input("Enter any number: "))
for i in range(y):
    z = int(input("Enter any number: "))
    x.append(z)
a = int(input("Enter any number: "))
for j in range (y):
    b = a - x[j]
    print(b)
    if b in x:
        print([x[j],b])
        

    