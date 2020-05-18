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
        print("Fricking type something right you twat")

def createPlayer():
    def playerQuestions():
        statDict = {"att":0}
        statDict["att"] = input("If you live in a rural area, enter 3, but if in a city area, enter 0")
        playerPref = input("Were you more into academics or sports?")
        if(statDict["att"] == 3):
            print("You live in a rural area. Your attack increases by 1." + (playerDictionary["atk"] + 1))
        elif(statDict["att"] == 0):
            if(playerPref == "academics"):
                print("You were more interested in academics. Your magic attack raised by 1." + (playerDictionary["matk"] + 1))
            elif(playerPref == "sports"):
                print("You were more interested in sports. Your health increased by 2." + (playerDictionary["health"] + 2))
            else:
                print("That is not a valid answer")
        else:
            print("That is not a valid input.")
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
    return(playerDictionary)
player = createPlayer()
def stats():
    print(player["name"])
    print("Your level is: " , player["level"])
    print("Your health is: " , player["health"])
    print("Your physical defense is: " , player["pdef"])
    print("Your magical defense: " , player["mdef"])
    print("Your attack power is: " , player["atk"])
    print("Your magical attack power is: " , player["matk"])
    print("Beginning at stage: " , player["stageNum"])
stats()


def enemy_generator(playerLevel):
    nameList = ["Bob", "James", "Carl", "Xenowrath", "Rachaug", "Suroa", "Tunara"]
    enemyName = nameList[random.randint(0,6)]
    def low_level():
        lowEnemyStats = {"Attack": random.randint(0,3)*playerLevel + random.randint(-1*playerLevel,playerLevel), 
        "Defense": random.randint(0,3)*playerLevel + random.randint(-1*playerLevel,playerLevel), 
        "magAttack": random.randint(0,3)*playerLevel + random.randint(-1*playerLevel,playerLevel), 
        "magDefense": random.randint(0,3)*playerLevel + random.randint(-1*playerLevel,playerLevel), 
        "HP": random.randint(0,3)*playerLevel + random.randint(-1*playerLevel,playerLevel), 
        "EnemyName": enemyName}
        if(lowEnemyStats["Attack"] <= 0):
            lowEnemyStats["Attack"] = 0
        if(lowEnemyStats["Defense"] <= 0):
            lowEnemyStats["Defense"] = 0
        if(lowEnemyStats["magAttack"] <= 0):
            lowEnemyStats["magAttack"] = 0
        if(lowEnemyStats["magDefense"] <= 0):
            lowEnemyStats["magDefense"] = 0
        if(lowEnemyStats["HP"] <= 0):
            lowEnemyStats["HP"] = 1
        print("The enemy you are up against is named" + lowEnemyStats["EnemyName"])
        print(lowEnemyStats["EnemyName"] + " has an attack level of " , lowEnemyStats["Attack"])
        print(lowEnemyStats["EnemyName"] + " has a defense level of " , lowEnemyStats["Defense"])
        print(lowEnemyStats["EnemyName"] + " has a magic attack level of " , lowEnemyStats["magAttack"])
        print(lowEnemyStats["EnemyName"] + " has a magic defense level of " , lowEnemyStats["magDefense"])
        print(lowEnemyStats["EnemyName"] + " has " , lowEnemyStats["HP"] , " health")
        return(lowEnemyStats)
    
    def mid_level():
        midEnemyStats = {"Attack": random.randint(1,4)*playerLevel + random.randint(-1*playerLevel,playerLevel), 
        "Defense": random.randint(1,4)*playerLevel + random.randint(-1*playerLevel,playerLevel), 
        "magAttack": random.randint(1,4)*playerLevel + random.randint(-1*playerLevel,playerLevel), 
        "magDefense": random.randint(1,4)*playerLevel + random.randint(-1*playerLevel,playerLevel), 
        "HP": random.randint(1,4)*playerLevel + random.randint(-1*playerLevel,playerLevel), 
        "EnemyName": enemyName}
        if(midEnemyStats["Attack"] <= 0):
            midEnemyStats["Attack"] = 0
        if(midEnemyStats["Defense"] <= 0):
            midEnemyStats["Defense"] = 0
        if(midEnemyStats["magAttack"] <= 0):
            midEnemyStats["magAttack"] = 0
        if(midEnemyStats["magDefense"] <= 0):
            midEnemyStats["magDefense"] = 0
        if(midEnemyStats["HP"] <= 0):
            midEnemyStats["HP"] = 1
        print("The enemy you are up against is named " + midEnemyStats["EnemyName"])
        print(midEnemyStats["EnemyName"] + " has an attack level of " , midEnemyStats["Attack"])
        print(midEnemyStats["EnemyName"] + " has a defense level of " , midEnemyStats["Defense"])
        print(midEnemyStats["EnemyName"] + " has a magic attack level of " , midEnemyStats["magAttack"])
        print(midEnemyStats["EnemyName"] + " has a magic defense level of " , midEnemyStats["magDefense"])
        print(midEnemyStats["EnemyName"] + " has " , midEnemyStats["HP"] , " health")
        return(midEnemyStats)
    
    def high_level():
        highEnemyStats = {"Attack": random.randint(2,5)*playerLevel + random.randint(-1*playerLevel,playerLevel), 
        "Defense": random.randint(2,5)*playerLevel + random.randint(-1*playerLevel,playerLevel), 
        "magAttack": random.randint(2,5)*playerLevel + random.randint(-1*playerLevel,playerLevel), 
        "magDefense": random.randint(2,5)*playerLevel + random.randint(-1*playerLevel,playerLevel), 
        "HP": random.randint(2,5)*playerLevel + random.randint(-1*playerLevel,playerLevel), 
        "EnemyName": enemyName}
        if(highEnemyStats["Attack"] <= 0):
            highEnemyStats["Attack"] = 0
        if(highEnemyStats["Defense"] <= 0):
            highEnemyStats["Defense"] = 0
        if(highEnemyStats["magAttack"] <= 0):
            highEnemyStats["magAttack"] = 0
        if(highEnemyStats["magDefense"] <= 0):
            highEnemyStats["magDefense"] = 0
        if(highEnemyStats["HP"] <= 0):
            highEnemyStats["HP"] = 1
        print("The enemy you are up against is named " + highEnemyStats["EnemyName"])
        print(highEnemyStats["EnemyName"] + " has an attack level of " , highEnemyStats["Attack"])
        print(highEnemyStats["EnemyName"] + " has a defense level of " , highEnemyStats["Defense"])
        print(highEnemyStats["EnemyName"] + " has a magic attack level of " , highEnemyStats["magAttack"])
        print(highEnemyStats["EnemyName"] + " has a magic defense level of " , highEnemyStats["magDefense"])
        print(highEnemyStats["EnemyName"] + " has " , highEnemyStats["HP"] , " health")
        return(highEnemyStats)
    
    if(playerLevel >= 1 and playerLevel <= 5):
        low_level()
    elif(playerLevel >= 6 and playerLevel <= 10):
        mid_level()
    elif(playerLevel >= 11 and playerLevel <= 15):
        high_level()
    else:
        print("That is not a valid level")
        pass
        

enemy_generator(random.randint(1,15))   


