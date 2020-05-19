import random

def createPlayer():
    playerDictionary = {"name":input("Please input your name:") , 
    "level":1 , 
    "health":10 , 
    "pdef":random.randint(0, 3) ,
    "mdef":random.randint(0, 3) , 
    "atk":random.randint(0, 3) , 
    "matk":random.randint(0, 3) , 
    "gold":0 , 
    "weapon":"bare hands" , 
    "armor":"commoner clothes" , 
    "stageNum":1}
