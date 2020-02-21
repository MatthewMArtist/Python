




# def garden():
#     print("garden")
# def downstairs_hallway():
#     print("downstairs_hallway")
# def outside():
#     print("outside")
# def search_garage():
#     print("search garage")



# def garage():
#     print("garage. Enter 'garden', 'downstairs_hallway', 'outside' or 'search_garage'")
#     response = input("What do you do? ")
#     if response == "garden":
#         garden()
#     elif response == "downstairs_hallway":
#         downstairs_hallway()
#     elif response == "outside":
#         outside()
#     elif response == "search_garage":
#         search_garage()
#     else:
#         print("Invalid response")
#         garage()
# def searched_garage():
#     print("garage. Enter 'garden', 'downstairs_hallway' or 'outside'")
#     response = input("What do you do? ")
#     if response == "garden":
#         garden()
#     elif response == "downstairs_hallway":
#         downstairs_hallway()
#     elif response == "outside":
#         outside()
#     else:
#         print("Invalid response")
#         searched_garage()

# def search_garage():
#     print("search garage")
#     searched_garage()

# garage()

# # print(" -------------------")
# # print("|       |           |")
# # print("|       |           |")
# # print("|-------------------|")
# # print("|    |  ------------|")
# # print("|    | |            |")
# # print("|-------------------|")
# # print("|                   |")
# # print(" ------------------- ")

# print(" ---------------------------------------------------------------------------------------")
# print("|                                                                                       |")
# print("|")
# print("|")
# print("|")
# print("|")
# print("|")
# print("|")
# print("|")
# print("")
# print("")
# print("")
# print("")
# print("")
# print("")
# print("")
# print("")
# print("")
# print("")
# print("")
# print("")
# print("")


# def upstairs_hallway():
#     print("upstairs hallway. Enter 'bedroom' or 'bathroom' or 'downstairs hallway'?")
#     response = input("What do you do? ")
#     if response == "bathroom":
#         bathroom()
#     elif response == "bedroom":
#         bedroom()
#     elif response == "downstairs hallway":
#         stairs()
#     else:
#         print("Invalid response")
#         ()
# def bedroom():
#     print("bedroom. Enter 'upstairs hallway' or 'search'")
#     response = input("What do you do? ")
#     if response == "search":
#         search()
#     elif response == "upstairs hallway":
#         upstairs_hallway()
#     else:
#         print("Invalid response")
#         ()
# def bathroom():
#     print("bathroom. Enter 'upstairs hallway' or 'search')
#     response = input("What do you do? ")
#     if response == "search":
#         search()
#     elif response == "upstairs hallway":
#         upstairs_hallway()
#     else:
#         print("Invalid response")
#         ()

import colorama
from colorama import Fore, Style, init
init(autoreset=True)
#import time

# Challenge 1: Lounge/Medical Pack
​
def challenge_lounge(): 
    print(Fore.MAGENTA + "If you drop me, I'm sure to crack. Give me a smile, and I'll always smile back.")
    response = input("What am I? > ")
    if response == "A Mirror" or response == "a mirror" or response == "mirror" or response == "A mirror" or response == "a Mirror" or response == "Mirror":
        print("Congratulations, you have unlocked the " + Fore.MAGENTA + "Medical Pack!")
        searched_lounge()
    else:
        print("Your answer is incorrect, please try again.")
​
#-------------------------------------------------------------------------------------------------------------#
# Challenge 2: Dining Room/Water Purification Tablets
def challenge_dining_room(): 
    print(Fore.MAGENTA + "What five-letter word becomes shorter when you add two letters to it?.")
    response = input("What's your answer? > ")
    if response == "Short" or response == "short":
        print("Congratulations, you have unlocked the " + Fore.MAGENTA + "Water Purification Tablets!")
        searched_dining_room()                    
    else:
        print("Your answer is incorrect, please try again")
​
#-------------------------------------------------------------------------------------------------------------#
# Challenge 3: Kitchen/Food 
​
def challenge_kitchen(): 
        print(Fore.MAGENTA + "The person who makes it has no need for it. The person who purchases it does not use it. The person who does use it does not know he or she is.")
        response = input("What is it? > ")
        if response == "A Coffin" or response == "a coffin" or response == "coffin" or response == "A coffin" or response == "a Coffin" or response == "Coffin":
            print("Congratulations, you have unlocked the " + Fore.MAGENTA + "Food" + Style.RESET_ALL + "and" + Fore.MAGENTA + "...")
            searched_kitchen()
        else:
            print("Your answer is incorrect, please try again.")

            
#-------------------------------------------------------------------------------------------------------------#
# Challenge 5: Garden/Water
​
def challenge_garden(): 
    print(Fore.MAGENTA + "The more you take, the more you leave behind.")
    response = input("What am I? > ")
    if response == "Footprints" or response == "footprints":
        print("Congratulations, you have unlocked the " + Fore.MAGENTA + "Water!")
        searched_garden()
    else:
        print("Your answer is incorrect, please try again.")
​
#-------------------------------------------------------------------------------------------------------------#
# Challenge 6: Garage/Matches + Fuel
​
def challenge_garage(): 
    print(Fore.MAGENTA + "What has many keys, but can't open a door?")
    response = input("What's your answer? > ")
    if response == "A Piano" or response == "a piano" or response == "piano" or response == "A piano" or response == "a Piano" or response == "Piano":
        print("Congratulations, you have unlocked the " + Fore.MAGENTA + "Matches & Fuel" + Style.RESET_ALL + "and" + Fore.MAGENTA + "...")
        searched_garage()
    else:
        print("Your answer is incorrect, please try again.")
            
#-------------------------------------------------------------------------------------------------------------#
# Challenge 7: Bedroom/Clothing
​
def challenge_bedroom(): 
    print(Fore.MAGENTA + "Poor people have it. Rich people need it. If you eat it you die.")
    response = input("What is it? > ")
    if response == "Nothing" or response == "nothing":
        print("Congratulations, you have unlocked the " + Fore.MAGENTA + "Clothing!")
        searched_bedroom()
    else:
        print("Your answer is incorrect, please try again.")
            
#-------------------------------------------------------------------------------------------------------------#
# Challenge 8: Bathroom/Radiation Therapy Kit
​
def challenge_bathroom(): 
    print(Fore.MAGENTA + "What travels around the world, but stays in one spot?")
    response = input("What's your answer? > ")
    if response == "A Stamp" or response == "a stamp" or response == "stamp" or response == "A stamp" or response == "a Stamp" or response == "Stamp":
        print("Congratulations, you have unlocked the " + Fore.MAGENTA + "Radiation Therapy Kit!")
        searched_bathroom()
    else:
        print("Your answer is incorrect, please try again.")
​
#-------------------------------------------------------------------------------------------------------------#
# Challenge 9: Outside/Radio
​
def challenge_outside(): 
    print(Fore.MAGENTA + "I'm a God, a planet and a measurer of heat.")
    response = input("What am I? > ")
    if response == "Mercury" or response == "mercury":
        print("Congratulations, you have unlocked the " + Fore.MAGENTA + "Radio!")
        searched_outside()
    else:
        print("Your answer is incorrect, please try again.")
​
#-------------------------------------------------------------------------------------------------------------#
# Challenge 10: Garage/Weaponry
​
def challenge_garage_2(): 
    print(Fore.MAGENTA + "What is (5 x 62) + (75 x 12)?")
    response = input("What's your answer? > ")
    if response == 1210:
        print("Congratulations, you have unlocked the " + Fore.MAGENTA + "Weapon!")
        searched_garage()
    else:
        print("Your answer is incorrect, please try again.")
        
#-------------------------------------------------------------------------------------------------------------#
​
print(Fore.RED + "Welcome to Time Bomb.") 
​
player_name = input("What's your name? >")
print(Fore.CYAN + "Welcome to the apocalyspe, " + player_name + "! It’s the end of the world... Your time is ticking and you have to make it to your bunker in the garden before you’re obliterated. Collect 10 items along the way to ensure your survival. Happy hunting!") 
​
input("...are you ready to kick some ass? > ")
print(Fore.CYAN + "You’re lazing around on the sofa, a beer in hand and an apocalyptic survivalist documentary playing. You love this stuff, knowing  it will one day come in handy because the conspiracy theorists are definitely not a bunch of quacks. Suddenly, the TV goes blank and a newscaster appears. “There have been reports of nuclear bombs striking major cities around the world. Your city is next. You have 5 minutes to find a place of safety before…” Static appears on the screen. “Huh, I guess he’s a goner…” You mutter to yourself. “You’ve got this," + player_name + ". Remember your training…”")

def bathroom():
    print("bathroom. Enter 'hallway' or 'search_bathroom' ")
    response = input("What do you do? ")
    if response == "search_bathroom":
        search_bathroom()
    elif response == "hallway":
        hallway()
    else:
        print("Invalid response")
        bathroom()
def searched_bathroom():
    print("bathroom. Enter 'hallway'")
    response = input("What do you do? ")
    if response == "hallway":
        hallway()
    else:
        print("Invalid response")
        searched_bathroom()
def search_bathroom():
    print("Search_bathroom")
    challenge_bathroom()
    searched_bathroom()


def bedroom():
    print("bedroom. Enter 'hallway' or 'search_bedroom' ")
    response = input("What do you do? ")
    if response == "search_bedroom":
        search_bedroom()
    elif response == "hallway":
        hallway()
    else:
        print("Invalid response")
        bedroom()
def searched_bedroom():
    print("bedroom. Enter 'hallway'")
    response = input("What do you do? ")
    if response == "hallway":
        hallway()
    else:
        print("Invalid response")
        searched_bedroom()
def search_bedroom():
    print("Search bedroom")
    challenge_bedroom()
    searched_bedroom()


def outside():
    print("outside. Enter 'hallway' or 'search_outside'")
    response = input("What do you do? ")
    if response == "hallway":
        hallway()
    elif response == "search_outside":
        search_outside()
    else:
        print("Invalid response")
        outside()
def searched_outside():
    print("outside. Enter 'hallway'")
    response = input("What do you do? ")
    if response == "hallway":
        hallway()
    else:
        print("Invalid response")
        searched_outside()
def search_outside():
    print("Search_outside")
    challenge_outside()
    searched_outside()


def garden():
    print("garden. Enter 'hallway'")
    response = input("What do you do? ")
    if response == "hallway":
        hallway()
    else:
        print("Invalid response")
        garden()


def dining_room():
    print("dining_room. Enter 'hallway' or 'search_dining_room'")
    response = input("What do you do? ")
    if response == "hallway":
        hallway()
    elif response == "search_dining_room":
        search_dining_room()
    else:
        print("Invalid response")
        dining_room()
def searched_dining_room():
    print("dining_room. Enter 'hallway'")
    response = input("What do you do? ")
    if response == "hallway":
        hallway()
    else:
        print("Invalid response")
        searched_dining_room()
def search_dining_room():
    print("Search dining room")
    challenge_dining_room()
    searched_dining_room()

def kitchen():
    print("kitchen. Enter 'hallway', or 'search_kitchen'")
    response = input("What do you do? ")
    if response == "hallway":
        hallway()
    elif response == "search_kitchen":
        search_kitchen()
    else:
        print("Invalid response")
        kitchen()
def searched_kitchen():
    print("kitchen. Enter 'hallway'")
    response = input("What do you do? ")
    if response == "hallway":
        hallway()
    else:
        print("Invalid response")
        searched_kitchen()
def search_kitchen():
    print("Search kitchen")
    challenge_kitchen()
    searched_kitchen()

def garage():
    print("garage. Enter 'hallway' or 'search_garage'")
    response = input("What do you do? ")
    if response == "hallway":
        hallway()
    elif response == "search_garage":
        search_garage()
    else:
        print("Invalid response")
        garage()
def searched_garage():
    print("garage. Enter 'hallway'")
    response = input("What do you do? ")
    if response == "hallway":
        hallway()
    else:
        print("Invalid response")
        searched_garage()
def search_garage():
    print("Search garage")
    challenge_garage()
    searched_garage()


def hallway():
    print("hallway. Enter 'garage', 'outside','bathroom', 'bedroom', 'dining_room', 'garden', 'lounge' or 'kitchen'.")
    response = input("What do you do? ")
    if response == "garage":
        garage()
    elif response == "outside":
        outside()
    elif response == "dining_room":
        dining_room()
    elif response == "kitchen":
        kitchen()
    elif response == "bathroom":
        bathroom()
    elif response == "bedroom":
        bedroom()
    elif response == "lounge":
        lounge()
    elif response == "garden":
        garden()
    else:
        print("Invalid response")
        hallway()


def lounge():
    print("lounge. Enter 'hallway' or 'search_lounge'")
    response = input("What do you do? ")
    if response == "hallway":
        hallway()
    elif response == "search_lounge":
        search_lounge()
    else:
        print("Invalid response")
        lounge()
def searched_lounge():
    print("lounge. Enter 'hallway'")
    response = input("What do you do? ")
    if response == "hallway":
        hallway()
    else:
        print("Invalid response")
        searched_lounge()
def search_lounge():
    print("Search lounge")
    challenge_lounge()
    searched_lounge()
lounge()