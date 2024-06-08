def cube(x):
    return x**3

l = [1,3,5,7,9,11]

newl = list(map(lambda x:x**3,l)) # take two argument one is function and other is object
print(newl)