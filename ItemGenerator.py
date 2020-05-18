import random
def itemCreation(playerLevel:5):

    def itemNameGenerator(category):
        if category == 'Sword':
            swordGodNames = []
            godName = random.choice(swordGodNames)
            swordFormats = [
                "The Sword of " + godName,
                "The Blade of " + godName,
                godName + "'s Edge", 
                godName + "'s Razor", 
                "The Decline of " + godName,
                godName + "'s Descent",
                "The Battle of " + godName + " and " + godName2]

        if category == 'Bow':
            bowGodNames = []
            godName = random.choice(bowGodNames)
            swordFormats = [
                "The Bow of " + godName,
                "The Secret of " + godName,
                godName + "'s Piercer", 
                godName + "'s Kiss", 
                "The Flight of " + godName,
                godName + "'s Disaster"]
            name = random.choice(swordFormats)

        if category == 'Staff':
            staffGodNames = []
            godName = random.choice(staffGodNames)
            swordFormats = [
                "The Staff of " + godName,
                "The Aura of " + godName,
                godName + "'s Will", 
                godName + "'s Desire", 
                "The Passion of " + godName,
                godName + "'s Fear"]
        
        if category == 'Tome':
            tomeGodNames = []
            godName = random.choice(tomeGodNames)
                "The Tome of " + godName,
                "The Knowledge of " + godName,
                godName + "'s Mind", 
                godName + "'s Mortal Grimoire", 
                "The Word of " + godName,
                godName + "'s Lessons"]

        if category == 'Armor':
            armorGodNames = []
            godName = random.choice(armorGodNames)
                "The Armor of " + godName,
                "The Clothes of " + godName,
                godName + "'s Skeleton", 
                godName + "'s Defiance", 
                "The Strength of " + godName,
                godName + "'s Fur"]
        return name
            

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