import random
def itemCreation(playerLevel:5):

    createdItem = {"name":None, "type":None, "itemHP":None, "itemATT":None, "itemDEF":None, "itemmATT":None, "itemmDEF":None}

    itemType = random.randint(1,10)

    if itemType in [1,2,3,4]:
        createdItem["name"] = itemNameGenerator()
        createdItem["itemHP"] = random.randint(0,3)*playerLevel + random.randint(-1*playerLevel,playerLevel)
        createdItem["itemATT"] = random.randint(0,3)*playerLevel + random.randint(-1*playerLevel,playerLevel)
        createdItem["itemDEF"] = random.randint(0,3)*playerLevel + random.randint(-1*playerLevel,playerLevel)
        createdItem["itemmATT"] = random.randint(0,3)*playerLevel + random.randint(-1*playerLevel,playerLevel)
        createdItem["itemmDEF"] = random.randint(0,3)*playerLevel + random.randint(-1*playerLevel,playerLevel)
        



print(itemCreation(5))