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

def createPlayer():
    playerDictionary = {"name":input("Please input your name:") , "level":1 , "health":10 , "pdef":random.randint(0, 3) , "mdef":random.randint(0, 3) , "atk":random.randint(0, 3) , "matk":random.randint(0, 3) , "gold":0}
    return(playerDictionary)
variable = createPlayer()
print("Your level is: " , variable["level"])
print("Your health is: ")
print("Your physical defense is: ")
print("Your magical defense: ")
print("Your attack power is: ")
print("Your magical attack power is: ")

def enemy_generator(playerLevel):
    nameList = ["Bob", "James", "Carl", "Xenowrath"]
    enemyName = nameList[random.randint(0,4)]
    print(playerLevel)
    if (playerLevel >= 1 and playerLevel <= 5):
        lowEnemyStuff = {"Attack": random.randint(0,3)*playerLevel + random.randint(-1*playerLevel,playerLevel), "Defense": random.randint(0,3)*playerLevel + random.randint(-1*playerLevel,playerLevel), "magAttack": random.randint(0,3)*playerLevel + random.randint(-1*playerLevel,playerLevel), "magDefense": random.randint(0,3)*playerLevel + random.randint(-1*playerLevel,playerLevel), "HP": random.randint(0,3)*playerLevel + random.randint(-1*playerLevel,playerLevel), "EnemyName": enemyName}
        print("The enemy you are up against " + lowEnemyStuff["EnemyName"])
        print(lowEnemyStuff["EnemyName"] + " has an attack level of " , lowEnemyStuff["Attack"])
        print(lowEnemyStuff["EnemyName"] + " has a defense level of " , lowEnemyStuff["Defense"])
        print(lowEnemyStuff["EnemyName"] + " has a magic attack level of " , lowEnemyStuff["magAttack"])
        print(lowEnemyStuff["EnemyName"] + " has a magic defense level of " , lowEnemyStuff["magDefense"])
        print(lowEnemyStuff["EnemyName"] + " has " , lowEnemyStuff["HP"] , " health")
    elif (playerLevel >= 6 and playerLevel <= 10):
        midEnemyStuff = {"Attack": random.randint(1,4)*playerLevel + random.randint(-1*playerLevel,playerLevel), "Defense": random.randint(1,4)*playerLevel + random.randint(-1*playerLevel,playerLevel), "magAttack": random.randint(1,4)*playerLevel + random.randint(-1*playerLevel,playerLevel), "magDefense": random.randint(1,4)*playerLevel + random.randint(-1*playerLevel,playerLevel), "HP": random.randint(1,4)*playerLevel + random.randint(-1*playerLevel,playerLevel), "EnemyName": enemyName}
        print("The enemy you are up against is named " + midEnemyStuff["EnemyName"])
        print(midEnemyStuff["EnemyName"] + " has an attack level of " , midEnemyStuff["Attack"])
        print(midEnemyStuff["EnemyName"] + " has a defense level of " , midEnemyStuff["Defense"])
        print(midEnemyStuff["EnemyName"] + " has a magic attack level of " , midEnemyStuff["magAttack"])
        print(midEnemyStuff["EnemyName"] + " has a magic defense level of " , midEnemyStuff["magDefense"])
        print(midEnemyStuff["EnemyName"] + " has " , midEnemyStuff["HP"] , " health")
    elif (playerLevel >= 11 and playerLevel <= 15):
        highEnemyStuff = {"Attack": random.randint(2,5)*playerLevel + random.randint(-1*playerLevel,playerLevel), "Defense": random.randint(2,5)*playerLevel + random.randint(-1*playerLevel,playerLevel), "magAttack": random.randint(2,5)*playerLevel + random.randint(-1*playerLevel,playerLevel), "magDefense": random.randint(2,5)*playerLevel + random.randint(-1*playerLevel,playerLevel), "HP": random.randint(2,5)*playerLevel + random.randint(-1*playerLevel,playerLevel), "EnemyName": enemyName}
        print("The enemy you are up against is named " + highEnemyStuff["EnemyName"])
        print(highEnemyStuff["EnemyName"] + " has an attack level of " , highEnemyStuff["Attack"])
        print(highEnemyStuff["EnemyName"] + " has a defense level of " , highEnemyStuff["Defense"])
        print(highEnemyStuff["EnemyName"] + " has a magic attack level of " , highEnemyStuff["magAttack"])
        print(highEnemyStuff["EnemyName"] + " has a magic defense level of " , highEnemyStuff["magDefense"])
        print(highEnemyStuff["EnemyName"] + " has " , highEnemyStuff["HP"] , " health")
    else:
        print("That is not a valid player level")
        pass 
        
enemy_generator(random.randint(1,16))   


