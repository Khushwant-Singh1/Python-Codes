import random
def game(comp, a):
    if comp == a:
        return None
    elif comp == "s":
        if a == "w":
            return False
        elif a == "g":
            return True
    elif comp == "w":
        if a == "s":
            return True
        elif a == "g":
            return False
    elif comp == "g":
        if a == "s":
            return False
        elif a == "w":
            return True    
print("Computer turn: Snake(s) Water(w) or Gun(g)?")
while True:
    rnum = random.randint(1,3)
    if rnum == 1:
        comp = "s"
    elif rnum == 2:
        comp = "w"
    elif rnum == 3:
        comp = "g"
    a = input("your turn: Snake(s) Water(w) or Gun(g)?")
    print (f"Computer chose: {comp}\nYou chose: {a}")
    if a.lower() == "exit":
        break
    x = game(comp, a)  
    if a.lower() == "exit":
        break 
    if x == None:
        print("The game is tie!")
    elif x :
        print("You Win!")
    else:
        print("You Lose!")