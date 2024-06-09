# newlist = [expression for item in iterable if condition == True0]
import random
import string

l = []
d = {}
for x in range(10):
    ran = random.randint(1, 100)
    res = ''.join(random.choices(string.ascii_letters))
    l.append(ran)
    d[ran] = str(res)

print(l)
print(d)

print([i for i in l if i % 2 == 0])  # list comprehension

print({j for j in l if j % 2 == 0})  # set comprehension

print(tuple(k for k in l if k % 2 == 0))  # tuple comprehension

print([i ** 2 for i in l])  # print the squared element from the list

print([(y ** 2, y + 5) for y in l])  # print the two or more expression in tuple

print([(z ** 2, z + 5) for z in l if z % 2 == 0])  # print the two or more expression in tuple

print({k1 ** 2: v1 for k1, v1 in d.items()})  # dictionary comprehension
