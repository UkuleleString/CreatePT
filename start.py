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
    playerDictionary = {"name":input("Please input your name:") , "level":1 , "health":10 , 
    "pdef":random.randint(0, 3) , "mdef":random.randint(0, 3) , "atk":random.randint(0, 3) , 
    "matk":random.randint(0, 3) , "gold":0 , "weapon":"bare hands" , "armor":"commoner clothes" , "stageNum":1}
    return(playerDictionary)
variable = createPlayer()
def stats():
print(variable["name"])
print("Your level is: " , variable["level"])
print("Your health is: " , variable["health"])
print("Your physical defense is: " , variable["pdef"])
print("Your magical defense: " , variable["mdef"])
print("Your attack power is: " , variable["atk"])
print("Your magical attack power is: " , variable["matk"])
print("Beginning at stage: " , variable["stageNum"])
stats()


def enemy_generator(playerLevel):
    nameList = ["Bob", "James", "Carl", "Xenowrath"]
    enemyName = nameList[random.randint(0,3)]
    if (playerLevel >= 1 and playerLevel <= 5):
        lowEnemyStats = {"Attack": random.randint(0,3)*playerLevel + random.randint(-1*playerLevel,playerLevel), "Defense": random.randint(0,3)*playerLevel + random.randint(-1*playerLevel,playerLevel), "magAttack": random.randint(0,3)*playerLevel + random.randint(-1*playerLevel,playerLevel), "magDefense": random.randint(0,3)*playerLevel + random.randint(-1*playerLevel,playerLevel), "HP": random.randint(0,3)*playerLevel + random.randint(-1*playerLevel,playerLevel), "EnemyName": enemyName}
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
        print("The enemy you are up against " + lowEnemyStats["EnemyName"])
        print(lowEnemyStats["EnemyName"] + " has an attack level of " , lowEnemyStats["Attack"])
        print(lowEnemyStats["EnemyName"] + " has a defense level of " , lowEnemyStats["Defense"])
        print(lowEnemyStats["EnemyName"] + " has a magic attack level of " , lowEnemyStats["magAttack"])
        print(lowEnemyStats["EnemyName"] + " has a magic defense level of " , lowEnemyStats["magDefense"])
        print(lowEnemyStats["EnemyName"] + " has " , lowEnemyStats["HP"] , " health")
    elif (playerLevel >= 6 and playerLevel <= 10):
        midEnemyStats = {"Attack": random.randint(1,4)*playerLevel + random.randint(-1*playerLevel,playerLevel), "Defense": random.randint(1,4)*playerLevel + random.randint(-1*playerLevel,playerLevel), "magAttack": random.randint(1,4)*playerLevel + random.randint(-1*playerLevel,playerLevel), "magDefense": random.randint(1,4)*playerLevel + random.randint(-1*playerLevel,playerLevel), "HP": random.randint(1,4)*playerLevel + random.randint(-1*playerLevel,playerLevel), "EnemyName": enemyName}
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
    elif (playerLevel >= 11 and playerLevel <= 15):
<<<<<<< HEAD
        highEnemyStats = {"Attack": random.randint(2,5)*playerLevel + random.randint(-1*playerLevel,playerLevel), "Defense": random.randint(2,5)*playerLevel + random.randint(-1*playerLevel,playerLevel), "magAttack": random.randint(2,5)*playerLevel + random.randint(-1*playerLevel,playerLevel), "magDefense": random.randint(2,5)*playerLevel + random.randint(-1*playerLevel,playerLevel), "HP": random.randint(2,5)*playerLevel + random.randint(-1*playerLevel,playerLevel), "EnemyName": enemyName}
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
=======
        highEnemyStuff = {"Attack": random.randint(2,5)*playerLevel + random.randint(-1*playerLevel,playerLevel), "Defense": random.randint(2,5)*playerLevel + random.randint(-1*playerLevel,playerLevel), "magAttack": random.randint(2,5)*playerLevel + random.randint(-1*playerLevel,playerLevel), "magDefense": random.randint(2,5)*playerLevel + random.randint(-1*playerLevel,playerLevel), "HP": random.randint(2,5)*playerLevel + random.randint(-1*playerLevel,playerLevel), "EnemyName": enemyName}
        print("The enemy you are up against is named " + highEnemyStuff["EnemyName"])
        print(highEnemyStuff["EnemyName"] + " has an attack level of " , highEnemyStuff["Attack"])
        print(highEnemyStuff["EnemyName"] + " has a defense level of " , highEnemyStuff["Defense"])
        print(highEnemyStuff["EnemyName"] + " has a magic attack level of " , highEnemyStuff["magAttack"])
        print(highEnemyStuff["EnemyName"] + " has a magic defense level of " , highEnemyStuff["magDefense"])
        print(highEnemyStuff["EnemyName"] + " has " , highEnemyStuff["HP"] , " health")
>>>>>>> 80dcd20c232f8d1ef6b3f2c4898ce7fdf18043b2
    else:
        print("That is not a valid player level")
        pass 
        return(lowEnemyStats)
        return(midEnemyStats)
        return(highEnemyStats)

enemy_generator(random.randint(1,15))   


