from functools import reduce


num = [ 8, 26, 47, 43, 75, 54, 22, 99, 7, 60]
def mysum(x,y):
    return x+y
sum = reduce(mysum, num)
print(sum)