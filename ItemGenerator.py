import random
def itemCreation(playerLevel:5):

    def itemNameGenerator(weaponType):

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