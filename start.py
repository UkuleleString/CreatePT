import random
from os import system, name 
from time import sleep 

def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear') 

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

    def playerQuestions():
        statDict = {"att":0}
        statDict["att"] = input("If you live in a rural area, enter 3, but if in a city area, enter 0 ")
        while True:
            if(statDict["att"] == 3):
                print("Rural area. Your physical attack increased by 1." + (playerDictionary["atk"] + 1))
                break
            elif(statDict["att"] == 0):
                print("You live in a city area. Physical defense increases by 1." + (playerDictionary["pdef"] + 1))
                break
            else:
                print("Not a valid input.")
                
        
        playerPref = input("Were you more into academics or sports?")
        while True:
            if(playerPref == "academics"):
                print("You were more interested in academics. Your magic attack raised by 1." + (playerDictionary["matk"] + 1))
                break
            elif(playerPref == "sports"):
                print("You were more interested in sports. Your health increased by 2." + (playerDictionary["health"] + 2))
                break
            else:
                print("Not a valid input.")
                
            
    #playerQuestions()
    return(playerDictionary)

def stats(entity, player=False):
    print("Name: " + entity["name"])
    if player == True:
        print("Your level is: " , entity["level"])
        print("Beginning at stage: " , entity["stageNum"])
        print("Your weapon is: " + entity['weapon']['name'])
        print("Your armor is: " + entity['armor']['name'])
    print("Your health is: " , entity["health"])
    print("Your physical defense is: " , entity["pdef"])
    print("Your magical defense: " , entity["mdef"])
    print("Your attack power is: " , entity["atk"])
    print("Your magical attack power is: " , entity["matk"])


#Enemy Generator function
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
        return(low_level())
    elif(playerLevel >= 6 and playerLevel <= 10):
        return(mid_level())
    elif(playerLevel >= 11 and playerLevel <= 15):
        return(high_level())
    else:
        print("That is not a valid level")
        pass

# Item Creation function
def itemCreation(itemType, playerLevel:5):
    '''Creates a random item based on player level'''

    def itemNameGenerator(category):
        '''Creates a random item name based on item type'''
        if category == 'Sword':
            swordGodNames = ['The Colonel', 'The Lionsmith','The Elegiast','The Sun-in-Rags','The Horned-Axe',
            'The Wolf Divided','The Madrugad']
            godName = random.choice(swordGodNames)
            godName2 = random.choice(swordGodNames)
            nameFormats = [
                "The Sword of " + godName,
                "The Blade of " + godName,
                godName + "'s Edge", 
                godName + "'s Razor", 
                "The Decline of " + godName,
                godName + "'s Descent",
                "The Battle of " + godName + " and " + godName2]
            name = random.choice(nameFormats)

        if category == 'Bow':
            bowGodNames = ['The Colonel', 'The Lionsmith','The Moth','The Velvet','The Malachite',
            'The Witch-and-Sister','The Vagabond','The Sister-and-Witch']
            godName = random.choice(bowGodNames)
            nameFormats = [
                "The Bow of " + godName,
                "The Secret of " + godName,
                godName + "'s Piercer", 
                godName + "'s Kiss", 
                "The Flight of " + godName,
                godName + "'s Disaster"]
            name = random.choice(nameFormats)

        if category == 'Staff':
            staffGodNames = ['The Malachite','The Witch-and-Sister','The Beachcomber','The Mother of Ants',
            'The Meniscate','The Horned-Axe']
            godName = random.choice(staffGodNames)
            nameFormats = [
                "The Staff of " + godName,
                "The Aura of " + godName,
                godName + "'s Will", 
                godName + "'s Desire", 
                "The Passion of " + godName,
                godName + "'s Fear"]
            name = random.choice(nameFormats)
        
        if category == 'Tome':
            tomeGodNames = ['The Door in the Eye','The Meniscate','The Madrugad','The Flowermaker',
            'The Forge of Days','The Vagabond']
            godName = random.choice(tomeGodNames)
            nameFormats = [
                "The Tome of " + godName,
                "The Knowledge of " + godName,
                godName + "'s Mind", 
                godName + "'s Mortal Grimoire", 
                "The Word of " + godName,
                godName + "'s Lessons"]
            name = random.choice(nameFormats)

        if category == 'Armor':
            armorGodNames = ['The Velvet','The Malachite','The Thunderskin','The Witch-and-Sister',
            'The Lionsmith','The Meniscate','The Madrugad','The Forge of Days','The Sister-and-Witch']
            godName = random.choice(armorGodNames)
            nameFormats = [
                "The Armor of " + godName,
                "The Clothes of " + godName,
                godName + "'s Skeleton", 
                godName + "'s Defiance", 
                "The Strength of " + godName,
                godName + "'s Fur"]
            name = random.choice(nameFormats)
        return name
            

    createdItem = {"name":None, "type":None, "itemHP":0, "itemATT":0, "itemDEF":0, "itemMagATT":0, "itemMagDEF":0}
    if itemType in ['Sword','Bow','Staff','Tome','Armor']:
        category = itemType
    else:
        typeList = ['Sword','Bow','Staff','Tome','Armor']
        category = random.choice(typeList)
    createdItem["type"] = category
    createdItem["name"] = itemNameGenerator(category)
    createdItem["itemHP"] = random.randint(0,3)*playerLevel + random.randint(-1*playerLevel,playerLevel)
    createdItem["itemATT"] = random.randint(0,3)*playerLevel + random.randint(-1*playerLevel,playerLevel)
    createdItem["itemDEF"] = random.randint(0,3)*playerLevel + random.randint(-1*playerLevel,playerLevel)
    createdItem["itemMagATT"] = random.randint(0,3)*playerLevel + random.randint(-1*playerLevel,playerLevel)
    createdItem["itemMagDEF"] = random.randint(0,3)*playerLevel + random.randint(-1*playerLevel,playerLevel)
        
    return createdItem

def roomGenerator(playerDictionary, stageNumber):
    '''Generates levels for players'''

    #Introduces new room
    print("The room is dark, dank, and has an enemy/enemies!")
    print()
    enemyDicts = {}
    for i in range(1,random.randint(2,4)):
        enemyDicts[i] = enemy_generator(playerDictionary['level'])
        print()
    enemies = len(enemyDicts)
    input()
    clear()

    def damageCalculator(attackerDict=createPlayer(), weapon=itemCreation('sword',1), defenderDict=enemy_generator(1), armor=itemCreation('armor',1), magic=False):
        if magic == False:
            print(attackerDict["name"] + "'s attack is ",attackerDict["atk"] + weapon['itemATT'])
            print(defenderDict["name"] + "'s defense is ", defenderDict["pdef"] + armor['itemDEF'])
            print(attackerDict['name'] + " attacks with their " + weapon['name'])
            return attackerDict["atk"] + weapon['itemATT'] - defenderDict["pdef"] + armor['itemDEF']
        else:
            print(attackerDict["name"] + "'s attack is ",attackerDict["matk"] + weapon['itemMagATT'])
            print(defenderDict["name"] + "'s defense is ", defenderDict["mdef"]  + armor['itemMagDEF'])
            print(attackerDict['name'] + " attacks with their " + weapon['name'])
            return attackerDict["matk"] + weapon['itemMagATT'] - defenderDict["mdef"] + armor['itemMagDEF']

    def playerAttack(magic):
        clear()
        print("Choose an enemy to attack!")
        for i in range(1, len(enemyDicts) + 1):
            print("To attack " + enemyDicts[i]["EnemyName"] + ", enter ", i)
        while True:
            playerTarget = input()
            if playerTarget in [1, 2, 3] and enemyDicts[playerTarget]['health'] == 0:
                break
            else: 
                print("Choose a valid target!")
        clear()
        enemyDicts[playerTarget]['health'] -= damageCalculator(playerDictionary, playerDictionary['weapon'],enemyDicts[playerTarget], magic)
        if enemyDicts[playerTarget]['health'] <= 0:
            enemies -= 1

    #Battle Sequence
    while True:
        temporaryDefense = {"pdef": 0, "mdef":0}
        playerAction = input("Are you going to 'ATTACK', 'MAGIC ATTACK', 'DEFEND', or look at someone's 'STATS'? ")
        if playerAction.lower() == 'attack':
            playerAttack(False)
        
        elif playerAction.lower() == 'magic attack':
            playerAttack(True)

        elif playerAction.lower() == 'defend':
            print("You prepare yourself for the enemy's onslaught. Your defense increases!")
            temporaryDefense['pdef'] = (playerDictionary['mdef']+playerDictionary['armor']['mdef'])/2
            temporaryDefense['mdef'] = (playerDictionary['mdef']+playerDictionary['armor']['mdef'])/2

        elif playerAction.lower() == 'stats':
            print("Whose stats do you want to check?")
            for i in range(1, len(enemyDicts) + 1):
                print("To attack " + enemyDicts[i]["EnemyName"] + ", enter ", i)
            print("To check yourself, enter 4!")
            while True:
                playerTarget = input()
                if playerTarget in [1, 2, 3]:
                    stats(enemyDicts[playerTarget])
                    break
                elif playerTarget == 4:
                    stats(playerDictionary, True)
                else: 
                    print("Choose a valid target!")
            continue

        if enemies == 0:
            print("After this long battle, you have defeated your opponents.")
            break

        print("The enemies are attacking!!!")
        for i in range(1, 1 + len(enemyDicts)):
            damageCalculator(attackerDict=enemyDicts[i],defenderDict=playerDictionary)
        
#Actual game and stuff starts here
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
    
    else: 
        print("Fricking type something right you twat")

#Storyline/intro
print("It was a peaceful day for you and your family. Maybe you were hiking or fishing, it's been so long you've started to forget.")
print("But you'll never forget their lifeless eyes staring at you. Their blood spattered across the remains of your once beautiful home.")
print("In that moment you swore revenge on the monster who killed them, Gerasis: Destroyer of Towns.")
print("Your quest for blood has brought you to the lair of Gerasis.")
print("You must fight and rise through the 14 levels of the lair before you can defeat him once and for all.")
print("Good luck, brave warrior!")
print(" ")
player = createPlayer()
stats()
for i in range(15):
    roomGenerator(player, i)