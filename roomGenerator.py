import random
from os import system, name 
from time import sleep 
  
# define our clear function 
def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear') 

def stats(entity):
    print(entity["name"])
    print("Your level is: " , entity["level"])
    print("Your health is: " , entity["health"])
    print("Your physical defense is: " , entity["pdef"])
    print("Your magical defense: " , entity["mdef"])
    print("Your attack power is: " , entity["atk"])
    print("Your magical attack power is: " , entity["matk"])
    print("Beginning at stage: " , entity["stageNum"])

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
    return playerDictionary

def enemy_generator(playerLevel):
    nameList = ["Bob", "James", "Carl", "Xenowrath", "Rachaug", "Suroa", "Tunara"]
    enemyName = nameList[random.randint(0,6)]
    def low_level():
        lowEnemyStats = {"atk": random.randint(0,3)*playerLevel + random.randint(-1*playerLevel,playerLevel), 
        "pdef": random.randint(0,3)*playerLevel + random.randint(-1*playerLevel,playerLevel), 
        "matk": random.randint(0,3)*playerLevel + random.randint(-1*playerLevel,playerLevel), 
        "mdef": random.randint(0,3)*playerLevel + random.randint(-1*playerLevel,playerLevel), 
        "health": random.randint(0,3)*playerLevel + random.randint(-1*playerLevel,playerLevel), 
        "EnemyName": enemyName}
        if(lowEnemyStats["atk"] <= 0):
            lowEnemyStats["atk"] = 0
        if(lowEnemyStats["pdef"] <= 0):
            lowEnemyStats["pdef"] = 0
        if(lowEnemyStats["matk"] <= 0):
            lowEnemyStats["matk"] = 0
        if(lowEnemyStats["mdef"] <= 0):
            lowEnemyStats["mdef"] = 0
        if(lowEnemyStats["health"] <= 0):
            lowEnemyStats["health"] = 1
        print("The enemy you are up against is named " + lowEnemyStats["EnemyName"])
        print(lowEnemyStats["EnemyName"] + " has an attack level of " , lowEnemyStats["atk"])
        print(lowEnemyStats["EnemyName"] + " has a defense level of " , lowEnemyStats["pdef"])
        print(lowEnemyStats["EnemyName"] + " has a magic attack level of " , lowEnemyStats["matk"])
        print(lowEnemyStats["EnemyName"] + " has a magic defense level of " , lowEnemyStats["mdef"])
        print(lowEnemyStats["EnemyName"] + " has " , lowEnemyStats["health"] , " health")
        return(lowEnemyStats)
    
    def mid_level():
        midEnemyStats = {"atk": random.randint(1,4)*playerLevel + random.randint(-1*playerLevel,playerLevel), 
        "pdef": random.randint(1,4)*playerLevel + random.randint(-1*playerLevel,playerLevel), 
        "matk": random.randint(1,4)*playerLevel + random.randint(-1*playerLevel,playerLevel), 
        "mdef": random.randint(1,4)*playerLevel + random.randint(-1*playerLevel,playerLevel), 
        "health": random.randint(1,4)*playerLevel + random.randint(-1*playerLevel,playerLevel), 
        "EnemyName": enemyName}
        if(midEnemyStats["atk"] <= 0):
            midEnemyStats["atk"] = 0
        if(midEnemyStats["pdef"] <= 0):
            midEnemyStats["pdef"] = 0
        if(midEnemyStats["matk"] <= 0):
            midEnemyStats["matk"] = 0
        if(midEnemyStats["mdef"] <= 0):
            midEnemyStats["mdef"] = 0
        if(midEnemyStats["health"] <= 0):
            midEnemyStats["health"] = 1
        print("The enemy you are up against is named " + midEnemyStats["EnemyName"])
        print(midEnemyStats["EnemyName"] + " has an attack level of " , midEnemyStats["atk"])
        print(midEnemyStats["EnemyName"] + " has a defense level of " , midEnemyStats["pdef"])
        print(midEnemyStats["EnemyName"] + " has a magic attack level of " , midEnemyStats["matk"])
        print(midEnemyStats["EnemyName"] + " has a magic defense level of " , midEnemyStats["mdef"])
        print(midEnemyStats["EnemyName"] + " has " , midEnemyStats["health"] , " health")
        return(midEnemyStats)
    
    def high_level():
        highEnemyStats = {"atk": random.randint(2,5)*playerLevel + random.randint(-1*playerLevel,playerLevel), 
        "pdef": random.randint(2,5)*playerLevel + random.randint(-1*playerLevel,playerLevel), 
        "matk": random.randint(2,5)*playerLevel + random.randint(-1*playerLevel,playerLevel), 
        "mdef": random.randint(2,5)*playerLevel + random.randint(-1*playerLevel,playerLevel), 
        "health": random.randint(2,5)*playerLevel + random.randint(-1*playerLevel,playerLevel), 
        "EnemyName": enemyName}
        if(highEnemyStats["atk"] <= 0):
            highEnemyStats["atk"] = 0
        if(highEnemyStats["pdef"] <= 0):
            highEnemyStats["pdef"] = 0
        if(highEnemyStats["matk"] <= 0):
            highEnemyStats["matk"] = 0
        if(highEnemyStats["mdef"] <= 0):
            highEnemyStats["mdef"] = 0
        if(highEnemyStats["health"] <= 0):
            highEnemyStats["health"] = 1
        print("The enemy you are up against is named " + highEnemyStats["EnemyName"])
        print(highEnemyStats["EnemyName"] + " has an attack level of " , highEnemyStats["atk"])
        print(highEnemyStats["EnemyName"] + " has a defense level of " , highEnemyStats["pdef"])
        print(highEnemyStats["EnemyName"] + " has a magic attack level of " , highEnemyStats["matk"])
        print(highEnemyStats["EnemyName"] + " has a magic defense level of " , highEnemyStats["mdef"])
        print(highEnemyStats["EnemyName"] + " has " , highEnemyStats["health"] , " health")
        return(highEnemyStats)
    
    if(playerLevel >= 1 and playerLevel <= 5):
        return low_level()
    elif(playerLevel >= 6 and playerLevel <= 10):
        return mid_level()
    elif(playerLevel >= 11 and playerLevel <= 15):
        return high_level()
    else:
        print("That is not a valid level")
        pass

def roomGenerator(playerDictionary):
    '''Generates levels for players'''

    def damageCalculator(attackerDict=createPlayer(), weapon, defenderDict, armor, magic):
        if magic == False:
            print(attackerDict["name"]+ "'s attack is ",attackerDict["atk"])
            print(defenderDict["name"]+ "'s defense is ", defenderDict["pdef"])
            print("You attack with your")
            return attackerDict["atk"] - defenderDict["pdef"]
        else:
            print(attackerDict["name"]+ "'s attack is ",attackerDict["atk"])
            print(defenderDict["name"]+ "'s defense is ", defenderDict["pdef"])
            return attackerDict["matk"] - defenderDict["mdef"] 

    #Introduces new room
    print("The room is dark, dank, and has an enemy/enemies!")
    print()
    enemyDicts = {}
    for i in range(1,random.randint(2,4)):
        enemyDicts[i] = enemy_generator(playerDictionary['level'])
        print()
    input()
    clear()

    #Battle Sequence
    while True:
        playerAction = input("Are you going to 'ATTACK', 'MAGIC ATTACK', 'DEFEND', or look at someone's 'STATS'? ")
        if playerAction.lower() == 'attack':
            clear()
            print("Choose an enemy to attack!")
            for i in range(1, len(enemyDicts) + 1):
                print("To attack " + enemyDicts[i]["EnemyName"] + ", enter ", i)
            while True:
                playerTarget = input()
                if playerTarget in [1, 2, 3]:
                    break
                else: 
                    print("Choose a valid target!")
            clear()
            damage = damageCalculator(playerDictionary, playerDictionary['weapon'],enemyDicts[playerTarget], False)
        

roomGenerator(createPlayer())