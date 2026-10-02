#Name:Gavin Merrell
#Class: 5th Hour
#Assignment: Scenario 1

#Scenario 1:
#You are a programmer for a fledgling game developer. Your team lead has asked you
#to create a nested dictionary containing five enemy creatures (and their properties)
#for combat testing. Additionally, the testers are asking for a way to input changes
#to the enemy's damage values for balancing, as well as having it print those changes
#to confirm they went through.

#Other than damage which is required, it is up to you to decide what properties are
#important and the theme of the game.

enemydos = {
    "enemy 1" : {
        "Name" : "Skeleton",
        "Damage" : 3,
        "magic" : False,
        "armor" : 10,
    },

    "enemy 2": {
        "Name": "zombie",
        "Damage": 8,
        "Magic": False,
        "armor": 22,
    },

    "enemy 3": {
        "Name": "warlock",
        "Damage": 28,
        "magic": True,
        "armor": 7,
    },

    "enemy 4": {
        "Name": "gewblin",
        "Damage": 50,
        "magic": True,
        "armor": 200,
    },

    "enemy 5": {
        "Name": "battle healer",
        "Damage": 0,
        "magic": True,
        "armor": 5,
    },
}

print(enemydos)

newdmg5 = int(input("New Damage? "))
enemydos["enemy 5"].update({"Damage": newdmg5})
print(enemydos["enemy 5"]["Damage"])

newdmg4 = int(input("New Damage? "))
enemydos["enemy 4"].update({"Damage": newdmg4})
print(enemydos["enemy 4"]["Damage"])

newdmg3 = int(input("New Damage? "))
enemydos["enemy 3"].update({"Damage": newdmg3})
print(enemydos["enemy 3"]["Damage"])

newdmg2 = int(input("New Damage? "))
enemydos["enemy 2"].update({"Damage": newdmg2})
print(enemydos["enemy 2"]["Damage"])

newdmg1 = int(input("New Damage? "))
enemydos["enemy 1"].update({"Damage": newdmg1})
print(enemydos["enemy 1"]["Damage"])

print(enemydos)