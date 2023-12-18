def factoriial_recusive(n):
    if n == 1 or n == 0:
        return 1
    return n*factoriial_recusive(n-1)

x = int(input("Enter any number: "))
f = factoriial_recusive(x)
print(f)