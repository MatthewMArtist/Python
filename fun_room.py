print("you are an adventuror in a fantasy land.")
name = input("What is your name?: ")
fantasy_class = input("what is your class (fighter, wizard, barbarian, rogue, bard)?: ")

import random
power = random.randint(1,100)
import random
skill = random.randint(1,100)

armour = 1
magic = 1
strength = 1
stealth = 1
music = 1

print("your are a {} with a power of {} and a skill of {}.".format(fantasy_class,power,skill))

if fantasy_class == "fighter":
    import random
    armour = random.randint(1,100)
    print("you have {} armour.".format(armour))
if fantasy_class == "wizard":
    import random
    magic = random.randint(1,100)
    print("you have {} magical skill.".format(magic))
if fantasy_class == "barbarian":
    import random
    strength = random.randint(1,100)
    print("you have {} strength.".format(strength))
if fantasy_class == "rogue":
    import random
    stealth = random.randint(1,100)
    print("you have {} stealth.".format(stealth))
if fantasy_class == "bard":
    import random
    music = random.randint(1,100)
    print("you have {} musical skill.".format(music))

location = input("Where are you (castle, forest, hills, city, plains)?: ")