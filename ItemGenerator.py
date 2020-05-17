import random
def itemCreation(playerLevel:5):

    def itemNameGenerator(category):
        offensiveGodNames = []
        if category == 'Sword':
            nameFormat = random.choice()
            if nameFormat == 0:
                return "The Sword of " + offensiveGodNames
            elif nameFormat == 1:
                return "The Blade of " + offensiveGodNames
            elif nameFormat == 2:
                return offensiveGodNames + "'s Edge"
            elif nameFormat == 3:
                return offensiveGodNames + "'s Razor"
            elif nameFormat == 4:
                return "The Decline of " + offensiveGodNames
            elif nameFormat == 5:
                return offensiveGodNames + "'s Descent"
            

    createdItem = {"name":None, "type":None, "itemHP":None, "itemATT":None, "itemDEF":None, "itemmATT":None, "itemmDEF":None}

    typeList = ['Sword','Bow','Staff','Tome','Armor']
    category = random.choice(typeList)
    createdItem["type"] = category
    createdItem["name"] = itemNameGenerator(category)
        createdItem["itemHP"] = random.randint(0,3)*playerLevel + random.randint(-1*playerLevel,playerLevel)
        createdItem["itemATT"] = random.randint(0,3)*playerLevel + random.randint(-1*playerLevel,playerLevel)
        createdItem["itemDEF"] = random.randint(0,3)*playerLevel + random.randint(-1*playerLevel,playerLevel)
        createdItem["itemmATT"] = random.randint(0,3)*playerLevel + random.randint(-1*playerLevel,playerLevel)
        createdItem["itemmDEF"] = random.randint(0,3)*playerLevel + random.randint(-1*playerLevel,playerLevel)
        
    return createdItem


print(itemCreation(5))