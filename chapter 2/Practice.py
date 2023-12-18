# # WAP to create a dictionary of hindi words with values as their english translation provide user with an option to look it up
# a={
#     "kitaab" : "book",
#     "raja" : "king",
#     "rajya" : "state",
#     "log" : "people"
# }
# print("Hindi words in the dictionary: ", a.keys() )
# b= input("Enter any word: ")
# print("here is the translation of the hindi word: ", a.get(b))

# # WAP to input numbers fron the user and display all the unique numbers(once)

# b=set()
# a=int(input("how many times you want to enter number: "))
# for i in range(a):
#     c=int(input('Enter the number you want to add:'))
#     b.add(c)
# print(b)

# Create an empty dictionary. Allow 4 friends to enter their favourite language as values and use keys as theirs names. Assume that the names are unique

lang = {}
a=int(input("how many times you want to enter name: "))
for i in range (a):
    b = input("Enter names: ")
    c = input("enter their favourite language: ")
    for y in range (a):
        lang[b] = c
print(lang)