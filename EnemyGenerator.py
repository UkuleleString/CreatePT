import pickle
import random

def enemy_generator(playerLevel):
    nameList = ["Bob", "James", "Carl", "Xenowrath"]
    enemyName = nameList[random.randint(0,4)]
    print(playerLevel)
    if (playerLevel >= 1 and playerLevel <= 5):
        lowEnemyStuff = {"Attack": random.randint(0,3)*playerLevel + random.randint(-1*playerLevel,playerLevel), "Defense": random.randint(0,3)*playerLevel + random.randint(-1*playerLevel,playerLevel), "magAttack": random.randint(0,3)*playerLevel + random.randint(-1*playerLevel,playerLevel), "magDefense": random.randint(0,3)*playerLevel + random.randint(-1*playerLevel,playerLevel), "HP": random.randint(0,3)*playerLevel + random.randint(-1*playerLevel,playerLevel), "EnemyName": enemyName}
        print("The enemy you are up against is named " + lowEnemyStuff["EnemyName"])
        print("The enemy you are up against has an attack level of " , lowEnemyStuff["Attack"])
        print("The enemy you are up against has a defense level of " , lowEnemyStuff["Defense"])
        print("The enemy you are up against has a magic attack level of " , lowEnemyStuff["magAttack"])
        print("The enemy you are up against has a magic defense level of " , lowEnemyStuff["magDefense"])
        print("The enemy you are up against has " , lowEnemyStuff["HP"] , " health")
    elif (playerLevel >= 6 and playerLevel <= 10):
        midEnemyStuff = {"Attack": random.randint(1,4)*playerLevel + random.randint(-1*playerLevel,playerLevel), "Defense": random.randint(1,4)*playerLevel + random.randint(-1*playerLevel,playerLevel), "magAttack": random.randint(1,4)*playerLevel + random.randint(-1*playerLevel,playerLevel), "magDefense": random.randint(1,4)*playerLevel + random.randint(-1*playerLevel,playerLevel), "HP": random.randint(1,4)*playerLevel + random.randint(-1*playerLevel,playerLevel), "EnemyName": enemyName}
        print("The enemy you are up against is named " + midEnemyStuff["EnemyName"])
        print("The enemy you are up against has an attack level of " , midEnemyStuff["Attack"])
        print("The enemy you are up against has a defense level of " , midEnemyStuff["Defense"])
        print("The enemy you are up against has a magic attack level of " , midEnemyStuff["magAttack"])
        print("The enemy you are up against has a magic defense level of " , midEnemyStuff["magDefense"])
        print("The enemy you are up against has " , midEnemyStuff["HP"] , " health")
    elif (playerLevel >= 11 and playerLevel <= 15):
        highEnemyStuff = {"Attack": random.randint(2,5)*playerLevel + random.randint(-1*playerLevel,playerLevel), "Defense": random.randint(2,5)*playerLevel + random.randint(-1*playerLevel,playerLevel), "magAttack": random.randint(2,5)*playerLevel + random.randint(-1*playerLevel,playerLevel), "magDefense": random.randint(2,5)*playerLevel + random.randint(-1*playerLevel,playerLevel), "HP": random.randint(2,5)*playerLevel + random.randint(-1*playerLevel,playerLevel), "EnemyName": enemyName}
        print("The enemy you are up against is named " + highEnemyStuff["EnemyName"])
        print("The enemy you are up against has an attack level of " , highEnemyStuff["Attack"])
        print("The enemy you are up against has a defense level of " , highEnemyStuff["Defense"])
        print("The enemy you are up against has a magic attack level of " , highEnemyStuff["magAttack"])
        print("The enemy you are up against has a magic defense level of " , highEnemyStuff["magDefense"])
        print("The enemy you are up against has " , highEnemyStuff["HP"] , " health")
    else:
        print("That is not a valid player level")
        
enemy_generator(random.randint(1,16))   