import pickle
import random
import tkinter

while True:
    print("********************")
    print("*     Welcome      *")
    print("*   To Our Game!   *")
    print("********************")

    print("Type 'Start' to start!")
    print("Type 'Load' to load your save file!")
    playerInput = input().lower()
    
    if (playerInput == "start"):
        print("started game")
        break

    elif (playerInput == "load"):
        print("loaded save")
        break
    
    else: 
        print("Fucking type something right you twat")

def enemy_generator():
     


<<<<<<< HEAD
thisIsADictionary = {"name":input("Please input your name:") , "health":10 , "pdef":random.randint(0, 3) , "mdef":random.randint(0, 3) , "atk":random.randint(0, 3) , "matk":random.randint(0, 3)}
=======
class createPlayer():
    def playerChar(name, weapon, level, stats):
        self.name = name 
        if (playerLevel >= 1 && playerLevel <= 5):
        lowEnemyStuff = {"Attack": }  
    def enemy_generator():
        if (playerLevel >= 1 && playerLevel <= 5):
        lowEnemyStuff = {"Attack": }
>>>>>>> b148d2352127ac895499a5aba348a79b228e910b
