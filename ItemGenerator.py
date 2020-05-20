import random
def itemCreation(playerLevel:5):
    '''Creates a random item based on player level'''

    def itemNameGenerator(category):
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

print(itemCreation(5))
