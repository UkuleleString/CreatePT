import pickle
import random

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
     

import tkinter
class createPlayer():
    def playerChar(name, weapon, level, stats):
       self.name = name 
=======
    if (playerLevel >= 1 && playerLevel <= 5):
        lowEnemyStuff = {"Attack": }  
>>>>>>> e8bd751ce3437a61a7cce02708c652b2a7eae437
