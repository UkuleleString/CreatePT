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

playerDictionary = {"name":input("Please input your name:") , "health":10 , "pdef":random.randint(0, 3) , "mdef":random.randint(0, 3) , "atk":random.randint(0, 3) , "matk":random.randint(0, 3)}
def createPlayer(playerDictionary):
    print(playerDictionary["name"])
