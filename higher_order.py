# Higher Order Function = a) function that either:
#                         1. accepts a function as an argujment
#                                 or
#                         2. return a function
#                             (In python, function are also treated as objects)
def loud (text):
    return text.upper()

def queit(text):
    return text.lower()

def hello(func):
    text = func("Hello World")
    print(text)

hello(loud)
hello(queit)

def divisor(x):
    def dividend(y):
        return y/x
    return dividend

divide = divisor(2)
print(divide(10))