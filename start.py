import random
from os import system, name 
from time import sleep 

def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear') 
#Create player functions
def createPlayer():
    playerDictionary = {"name":input("Please input your name:") , 
    "level":1 , 
    "health":10 , 
    "pdef":random.randint(0, 3) ,
    "mdef":random.randint(0, 3) , 
    "atk":random.randint(0, 3) , 
    "matk":random.randint(0, 3) , 
    "gold":0 , 
    "weapon":{} , 
    "armor":{} , 
    "stageNum":1}
    

    def playerQuestions():
        while True:
            statDict = input("Do you live in a rural area or a city area? ")
            if(statDict == "rural" or statDict == "Rural"):
                playerDictionary["atk"] += 1
                print("Rural area. Your physical attack increased by 1.")
                break
            elif(statDict == "city" or statDict == "City"):
                playerDictionary["pdef"] += 1
                print("You live in a city area. Physical defense increases by 1.")
                break
            else:
                print("Not a valid input.")
                
        
        while True:
            playerPref = input("Were you more into academics or sports? ")
            if(playerPref == "academics" or playerPref == "Academics"):
                playerDictionary["matk"] += 1
                print("You were more interested in academics. Your magic attack raised by 1.")
                break
            elif(playerPref == "sports" or playerPref == "Sports"):
                playerDictionary["health"] += 2
                print("You were more interested in sports. Your health increased by 2.")
                break
            else:
                print("Not a valid input.")
                
            
    playerQuestions()
    return(playerDictionary)

def stats(entity, player=False):
    print("Name: " + entity["name"])
    if player == True:
        print("level: " , entity["level"])
        print("Stage: " , entity["stageNum"])
        print("Weapon: " + entity['weapon']['name'])
        print(entity['weapon'])
        print("Armor: " + entity['armor']['name'])
        print(entity['armor'])
    print("Health: " , entity["health"])
    print("Attack: ", entity['atk'])
    print("Magical Attack: ", entity['matk'])
    print("Physical defense: " , entity["pdef"])
    print("Magical defense: " , entity["mdef"])
    input("Press enter to continue...")
    clear()


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
        "name": enemyName}
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
        print("The enemy you are up against is named " + lowEnemyStats["name"])
        print(lowEnemyStats["name"] + " has an attack level of " , lowEnemyStats["atk"])
        print(lowEnemyStats["name"] + " has a defense level of " , lowEnemyStats["pdef"])
        print(lowEnemyStats["name"] + " has a magic attack level of " , lowEnemyStats["matk"])
        print(lowEnemyStats["name"] + " has a magic defense level of " , lowEnemyStats["mdef"])
        print(lowEnemyStats["name"] + " has " , lowEnemyStats["health"] , " health")
        return(lowEnemyStats)
    
    def mid_level():
        midEnemyStats = {"atk": random.randint(1,4)*playerLevel + random.randint(-1*playerLevel,playerLevel), 
        "pdef": random.randint(1,4)*playerLevel + random.randint(-1*playerLevel,playerLevel), 
        "matk": random.randint(1,4)*playerLevel + random.randint(-1*playerLevel,playerLevel), 
        "mdef": random.randint(1,4)*playerLevel + random.randint(-1*playerLevel,playerLevel), 
        "health": random.randint(1,4)*playerLevel + random.randint(-1*playerLevel,playerLevel), 
        "name": enemyName}
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
        print("The enemy you are up against is named " + midEnemyStats["name"])
        print(midEnemyStats["name"] + " has an attack level of " , midEnemyStats["atk"])
        print(midEnemyStats["name"] + " has a defense level of " , midEnemyStats["pdef"])
        print(midEnemyStats["name"] + " has a magic attack level of " , midEnemyStats["matk"])
        print(midEnemyStats["name"] + " has a magic defense level of " , midEnemyStats["mdef"])
        print(midEnemyStats["name"] + " has " , midEnemyStats["health"] , " health")
        return(midEnemyStats)
    
    def high_level():
        highEnemyStats = {"atk": random.randint(2,5)*playerLevel + random.randint(-1*playerLevel,playerLevel), 
        "pdef": random.randint(2,5)*playerLevel + random.randint(-1*playerLevel,playerLevel), 
        "matk": random.randint(2,5)*playerLevel + random.randint(-1*playerLevel,playerLevel), 
        "mdef": random.randint(2,5)*playerLevel + random.randint(-1*playerLevel,playerLevel), 
        "health": random.randint(2,5)*playerLevel + random.randint(-1*playerLevel,playerLevel), 
        "name": enemyName}
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
        print("The enemy you are up against is named " + highEnemyStats["name"])
        print(highEnemyStats["name"] + " has an attack level of " , highEnemyStats["atk"])
        print(highEnemyStats["name"] + " has a defense level of " , highEnemyStats["pdef"])
        print(highEnemyStats["name"] + " has a magic attack level of " , highEnemyStats["matk"])
        print(highEnemyStats["name"] + " has a magic defense level of " , highEnemyStats["mdef"])
        print(highEnemyStats["name"] + " has " , highEnemyStats["health"] , " health")
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
            

    createdItem = {"name":None, "type":None, "itemHP":0, "atk":0, "pdef":0, "matk":0, "mdef":0}
    if itemType in ['Sword','Bow','Staff','Tome','Armor']:
        category = itemType
    else:
        typeList = ['Sword','Bow','Staff','Tome','Armor']
        category = random.choice(typeList)
    createdItem["type"] = category
    createdItem["name"] = itemNameGenerator(category)
    createdItem["itemHP"] = random.randint(0,3)*playerLevel + random.randint(-1*playerLevel,playerLevel)

    createdItem["atk"] = random.randint(0,3)*playerLevel + random.randint(-1*playerLevel,playerLevel)
    if category in ['Sword', 'Bow']:
        createdItem['atk'] += random.randint(2,4)*playerLevel

    createdItem["pdef"] = random.randint(0,3)*playerLevel + random.randint(-1*playerLevel,playerLevel)
    if category == 'Armor':
        createdItem['pdef'] += random.randint(2,4)*playerLevel

    createdItem["matk"] = random.randint(0,3)*playerLevel + random.randint(-1*playerLevel,playerLevel)
    if category in ['Staff', 'Tome']:
        createdItem['matk'] += random.randint(2,4)*playerLevel

    createdItem["mdef"] = random.randint(0,3)*playerLevel + random.randint(-1*playerLevel,playerLevel)
    if category == 'Armor':
        createdItem['mdef'] += random.randint(2,4)*playerLevel

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
    input("Press enter to continue...")
    clear()

    def damageCalculator(attackerDict={"name":'Mary' , "health":10 , "pdef":0,"mdef":0 , "atk":0 , "matk":0}, weapon=itemCreation('Sword',1), defenderDict=enemy_generator(1), armor=itemCreation('Armor',1), magic=False):
        if magic == False:
            print(attackerDict["name"] + "'s attack is ", (attackerDict["atk"] + weapon['atk']))
            print(defenderDict["name"] + "'s defense is ", (defenderDict["pdef"] + armor['pdef']))
            print(attackerDict['name'] + " attacks with their " + weapon['name'])
            if random.randint(0,50) == 34:
                return attackerDict["atk"] + weapon['atk']
            else:
                return attackerDict["atk"] + weapon['atk'] - defenderDict["pdef"] - armor['pdef']
        else:
            print(attackerDict["name"] + "'s attack is ", (attackerDict["matk"] + weapon['matk']))
            print(defenderDict["name"] + "'s defense is ", (defenderDict["mdef"]  + armor['mdef']))
            print(attackerDict['name'] + " attacks with their " + weapon['name'])
            if random.randint(0,50) == 34:
                return attackerDict["matk"] + weapon['matk']
            else:
                return attackerDict["matk"] + weapon['matk'] - defenderDict["mdef"] - armor['mdef']

    def playerAttack(magic, enemyDicts, playerDictionary):
        clear()
        print("Choose an enemy to attack!")
        for i in range(1, len(enemyDicts) + 1):
            print("To attack " + enemyDicts[i]['name'] + ", HP: ", enemyDicts[i]["health"] ,", enter ", i)
        while True:
            playerTarget = int(input())
            if playerTarget in [1, 2, 3] and enemyDicts[playerTarget]['health'] > 0:
                break
            else: 
                print("Choose a valid target!")
        clear()
        damage = damageCalculator(playerDictionary, playerDictionary['weapon'],enemyDicts[playerTarget], magic=magic)
        if damage > 0:   
            enemyDicts[playerTarget]['health'] -= damage
        print(enemyDicts[playerTarget]['name'] + " is at ", enemyDicts[playerTarget]['health'], " health!")
        input("Press enter to continue...")
        return (enemyDicts, playerTarget)

    #Battle Sequence
    while True:
        clear()
        temporaryDefense = {"pdef": 0, "mdef":0}
        playerAction = input("Are you going to 'ATTACK', 'MAGIC ATTACK', 'DEFEND', or look at someone's 'STATS'? ")
        if playerAction.lower() == 'attack':
            playerAction = playerAttack(False, enemyDicts, playerDictionary)
            enemyDicts = playerAction[0]
            if enemyDicts[playerAction[1]]['health'] <= 0:
                enemies -= 1
            if enemies == 0:
                print("After this long battle, you have defeated your opponents.")
                input("Press enter to continue...")
                clear()
                break
        
        elif playerAction.lower() == 'magic attack':
            playerAction = playerAttack(True, enemyDicts, playerDictionary)
            enemyDicts = playerAction[0]
            if enemyDicts[playerAction[1]]['health'] <= 0:
                enemies -= 1
            if enemies == 0:
                print("After this long battle, you have defeated your opponents.")
                input("Press enter to continue...")
                clear()
                break

        elif playerAction.lower() == 'defend':
            print("You prepare yourself for the enemy's onslaught. Your defense increases!")
            temporaryDefense['pdef'] = (playerDictionary['mdef']+playerDictionary['armor']['mdef'])/2
            temporaryDefense['mdef'] = (playerDictionary['mdef']+playerDictionary['armor']['mdef'])/2
            input("Press enter to continue...")

        elif playerAction.lower() == 'stats':
            print("Whose stats do you want to check?")
            for i in range(1, len(enemyDicts) + 1):
                print("To attack " + enemyDicts[i]["name"] + ", enter ", i)
            print("To check yourself, enter 4!")
            while True:
                playerTarget = int(input())
                if playerTarget in [1, 2, 3]:
                    stats(enemyDicts[playerTarget])
                    break
                elif playerTarget == 4:
                    stats(playerDictionary, True)
                    break
                else: 
                    print("Choose a valid target!")
            continue

        else:
            print("What?")
            continue

        clear()
        print("The enemies are attacking!!!")
        for i in range(1, 1 + len(enemyDicts)):
            if enemyDicts[i]['health'] > 0:
                damage = damageCalculator(attackerDict=enemyDicts[i],defenderDict=playerDictionary,magic=random.choice([True,False]))
                if damage > 0:
                    playerDictionary['health'] -= damage
        print("You are at ", playerDictionary['health'], " health!")
        input("Press enter to continue...")
        if playerDictionary['health'] <= 0:
            clear()
            print("As you take your final breath, you curse Gerasis, but he feels nothing at all...")
            input("Press enter to end.")
            exit()

def gearGiver():
    player['weapon'] = itemCreation(random.choice(['Sword', 'Bow', 'Staff', 'Tome']), player['level'])
    player['armor'] = itemCreation('Armor', player['level'])
    print("You found: " + player['weapon']['name'])
    print(player['weapon']['type'] + ", Attack: " , player['weapon']['atk'], ", Magic Attack: ", player['weapon']['matk'])
    print("You found: " + player['armor']['name'])
    print(player['armor']['type'] + ", Defense: " , player['armor']['pdef'], ", Magic Defense: ", player['armor']['mdef'])
        
#Actual game and stuff starts here
while True:
    clear()
    print("********************")
    print("*     Welcome      *")
    print("*   To Our Game!   *")
    print("********************")

    print("Type 'Start' to start!")
    playerInput = input().lower()
    
    if (playerInput == "start"):
        clear()
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
input("Press enter to continue...")
clear()
gearGiver()
input("Press enter to continue...")
clear()
stats(player, True)
for i in range(1, 16):
    roomGenerator(player, i)
    print("On your way towards your foe, you've found some equipment")
    player['stageNum'] += 1
    player['level'] += 1
    gearGiver()
    input("Press enter to continue...")
    clear()
    player['health'] += random.randint(5,7)
    player['atk'] += random.randint(1,3)
    player['matk'] += random.randint(1,3)
    player['pdef'] += random.randint(1,3)
    player['mdef'] += random.randint(1,3)
    print("You leveled up!!!!!!")
    stats(player,True)