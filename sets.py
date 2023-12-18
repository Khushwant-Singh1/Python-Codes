a= {1,2,3,4,5,1}
print(type(a))
print(a)
# Impotant : this syntax will create an empty dictionary but not the empty set
b={p}
print(type(b))
# An empty set can be created using the below the syntax
c = set()
print(type(c))
# Adding value to empty set
c.add(4)
c.add(4)
c.add(4)
c.add(5) # Adding a value repeadly cannot change the value of the sets
c.add(5)
c.add(5)
c.add(8)
c.add(7)
c.add(11)
#c.add([4,5,6])
# c.add({4:python})  cannot add list or dictionary to the sets
c.add((4,5,6))
print(c)
print(len(c)) # print the length of this sets
# c.remove(5)
# print(c)
# print(c.pop())
# print(c)
print(c.intersection({8,11}))
print(c.union({8,11}))
# s={18, "18", "18"}
# print(s)
# se={20,20.0,"20"}
# print(len(se))
# print(se)
