'''
Snake,Gun,Water Game OR Rock,Paper,Scissor
'''

import random

def gameWin(comp,you):
    if(comp == you):
        return None  #No result
    elif(comp == "s"):
        if(you == "w"):
            return False #Lose
        elif(you == "g"):
            return True #Won
    elif(comp == "w"):
        if(you == "g"):
            return False #Lose
        elif(you == "s"):
            return True #Won
    elif(comp == "g"):
        if(you == "s"):
            return False #Lose
        elif(you == "w"):
            return True #Won

a=print("Comp Turn: Snake(s) Water(w) Gun(g):")
randNo = random.randint(0,2)  #random from 0,1,2
#print(randNo)
if(randNo == 0):
    comp="s"
elif(randNo == 1):
    comp="w"
else:
    comp="g"

you=input("Your Turn: Snake(s) Water(w) Gun(g):?")

print("You chose",you)
print("Comp chose",comp)

result = gameWin(comp,you)
if(result == True):
    print("You Won")
elif(result == False):
    print("You Lost")
else:
    print("Match Tied")