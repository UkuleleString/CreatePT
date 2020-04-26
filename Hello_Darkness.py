import time

def function():
    print("To make a function, use use 'def' to begin to define the function")

string = "this is a string"
thisIsAnInteger = 7
thisIsABoolean = True
thisIsAList = [5, 6, 7, 8]
thisIsADictionary = {"key":"value" , "five":5}

function()
print("This shows the value associated with the key in the dictionary: " + thisIsADictionary["key"])
print("This shows the value in the 2 spot of the list: " + thisIsAList[2])

class person(self, height, weight, gender, ethnicity):

    def __init__(self, height, weight, gender, ethnicity):
        self.height = height
        self.weight = weight
        personGender = gender
        personEthnicity = ethnicity

Mia = person("4'11","108 lbs", "female", "Mixed")

print("This is Mia's height: " + Mia.height)
print("This is Mia's weight: " + Mia.weight)

print("This will not work because you can't access this varable without the 'self' at the beginning.")
print(Mia.personGender)