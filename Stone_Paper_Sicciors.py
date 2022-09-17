# It's my first GAME !!!!   27 december 2021
import random
from os import system, name
from time import sleep
  
def clear():
  

    if name == 'nt':
        _ = system('cls')
  
    else:
        _ = system('clear')


def gamewin(you):
    comp = random.randint(1,3)
    if comp == you:
        return None
    elif comp == 1:
        print("Computer choose: Stone")
        if you == 3:
            return False
        else:
            return True
    elif comp == 2:
        print("Computer choose: Paper")

        if you == 3:
            return False
        else:
            return True
    elif comp == 3:
        print("Computer choose: Scissors")

        if you == 2:
            return False
        else:
            return True
    
    


z = True
while z:
    print("Welcome to Stone Paper & Scissors")
    a = input("You ready to play \n (y/n): ")
    if a == "y":
        clear()
        you = int(input("Choose Wisely: \n 1. Stone \n 2. Paper \n 3. Scissors\n"))
        if you == 1:
            print("You choose: Stone")
        elif you == 2:
            print("You choose: Paper")
        elif you == 3:
            print("You choose: Scissors")
        c = gamewin(you)
        if c == True:
            print("You Won!!!")
        elif c == False:
            print("You Lost")
        else:
            print("It's a fucking Tie")
        b = input("wanna Start again\n (y/n): ")
        if b == "y":
            clear()
            pass
        elif b == "n":
            break
    elif a == "n":
        print("Fuck off !!!") 
        break
    else:
        print("You choose invalid option")
        

  

   

