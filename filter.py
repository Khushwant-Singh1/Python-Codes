l =[12, 38, 9, 33, 5, 42, 47, 41, 43, 29]

def filter_func(n):
    return n%2 ==0

newl = list(filter(lambda x: x%2==0,l)) # takes two arguments predicate and iterable
print(newl)