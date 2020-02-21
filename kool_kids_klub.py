# import random
# password = random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9)

player_moves = 0

def challenge_completed():
    global player_moves
    if player_moves == 0:
        player_moves = 1
        print(player_moves)
        return
    if player_moves == 1:
        player_moves = 2
        print(player_moves)
        return
    if player_moves == 2:
        player_moves = 3
        print(player_moves)
        return
    if player_moves == 3:
        player_moves = 4
        print(player_moves)
        return
    if player_moves == 4:
        player_moves = 5
        print(player_moves)
        return
    if player_moves == 5:
        player_moves = 6
        print(player_moves)
        return
    if player_moves == 6:
        player_moves = 7
        print(player_moves)
        return
    if player_moves == 7:
        player_moves = 8
        print(player_moves)
        return
    if player_moves == 8:
        player_moves = 9
        print(player_moves)
        return
    if player_moves == 9:
        print("Nuclear Ending")
        quit()

room_clear = {
    "bathroom": "false",
    "bedroom": "false",
    "outside": "false",
    "dining_room": "false",
    "kitchen": "false",
    "garage": "false",
    "lounge": "false",
    "garden": "false"
    }
inventory = {
  "Water": "X",
  "Food + Cooking Equipment": "X",
  "Medical Pack": "X",
  "Matches + Fuel": "X",
  "Weapon": "X",
  "Radiation Therapy Kit": "X",
  "Clothing": "X",
  "Radio": "X"
}

sum1 = inventory.get("Water")
sum2 = inventory.get("Food + Cooking Equipment")
sum3 = inventory.get("Medical Pack")
sum4 = inventory.get("Matches + Fuel")
sum5 = inventory.get("Weapon")
sum6 = inventory.get("Radiation Therapy Kit")
sum7 = inventory.get("Clothing")
sum8 = inventory.get("Radio")

def checksum():
    if sum1 == "X":
        print("Dehydration Ending")
        return
    if sum2 == "X":
        print("Starvation Ending")
        return
    if sum3 == "X":
        print("Sickness Ending")
        return
    if sum4 == "X":
        print("Frozen Ending")
        return
    if sum5 == "X":
        print("Bandit Ending")
        return
    if sum6 == "X":
        print("Irradiated Ending")
        return
    if sum7 == "X":
        print("Elements Ending")
        return
    if sum8 == "X":
        print("Solitude Ending")
        return
    else:
        print("Born Survivor Ending")

def bathroom():
    print("bathroom. Enter 'hallway' or 'search_bathroom' ")
    x = room_clear.get("bathroom")
    response = input("What do you do? ")
    if response == "search_bathroom" and x == "false":
        search_bathroom()
    if response == "search_bathroom" and x == "true":
        print("You have already searched this room.")
        searched_bathroom()
    elif response == "hallway":
        hallway()
    else:
        print("Invalid response")
        bathroom()
def searched_bathroom():
    print("bathroom. Enter 'hallway' or 'search_bathroom'")
    x = room_clear.get("bathroom")
    response = input("What do you do? ")
    if response == "hallway":
        hallway()
    if response == "search_bathroom" and x == "true":
        print("This room has already been searched.")
        searched_bathroom()
    else:
        print("Invalid response")
        searched_bathroom()
def search_bathroom():
    print("Search_bathroom")
    challenge_completed()
    room_clear.update({"bathroom": "true"})
    searched_bathroom()


def bedroom():
    print("bedroom. Enter 'hallway' or 'search_bedroom' ")
    x = room_clear.get("bedroom")
    response = input("What do you do? ")
    if response == "search_bedroom" and x == "false":
        search_bedroom()
    if response == "search_bedroom" and x == "true":
        print("You have already searched this room.")
        searched_bedroom()
    elif response == "hallway":
        hallway()
    else:
        print("Invalid response")
        bedroom()
def searched_bedroom():
    print("bedroom. Enter 'hallway' or 'search_bedroom'")
    x = room_clear.get("bedroom")
    response = input("What do you do? ")
    if response == "hallway":
        hallway()
    if response == "search_bedroom" and x == "true":
        print("This room has already been searched.")
        searched_bedroom()
    else:
        print("Invalid response")
        searched_bedroom()
def search_bedroom():
    print("Search bedroom")
    challenge_completed()
    room_clear.update({"bedroom": "true"})
    searched_bedroom()


def outside():
    print("outside. Enter 'hallway' or 'search_outside'")
    x = room_clear.get("outside")
    response = input("What do you do? ")
    if response == "search_outside" and x == "false":
        search_outside()
    if response == "search_outside" and x == "true":
        print("You have already searched outside.")
        searched_outside()
    elif response == "search_outside":
        search_outside()
    else:
        print("Invalid response")
        outside()
def searched_outside():
    print("outside. Enter 'hallway' or 'search_outside'")
    x = room_clear.get("outside")
    response = input("What do you do? ")
    if response == "hallway":
        hallway()
    if response == "search_outside" and x == "true":
        print("This place has already been searched.")
        searched_outside()
    else:
        print("Invalid response")
        searched_outside()
def search_outside():
    print("Search_outside")
    challenge_completed()
    room_clear.update({"outside": "true"})
    searched_outside()


def garden():
    print("garden. Enter 'hallway', 'bunker' or 'search_garden'")
    x = room_clear.get("garden")
    response = input("What do you do? ")
    if response == "search_garden" and x == "false":
        search_garden()
    if response == "search_garden" and x == "true":
        print("You have already searched this room.")
        searched_garden()
    if response == "bunker":
        print("You are now in front of the bunker.")
        print("-show list of collected items-")
        bunker_question = input("Would you like to enter the bunker? WARNING: Once you enter the bunker, you won't be leaving for a while: ")
        if bunker_question == "yes":
            checksum()
        elif bunker_question == "no":
            garden()
        else:
            print("invalid response")
            garden()
    elif response == "hallway":
        hallway()
    else:
        print("Invalid response")
        garden()
def searched_garden():
    print("garden. Enter 'hallway' or 'search_garden'")
    x = room_clear.get("garden")
    response = input("What do you do? ")
    if response == "hallway":
        hallway()
    if response == "search_garden" and x == "true":
        print("This room has already been searched.")
        searched_garden()
    else:
        print("Invalid response")
        searched_garden()
def search_garden():
    print("Search_garden")
    challenge_completed()
    room_clear.update({"garden": "true"})
    searched_garden()


def dining_room():
    print("dining_room. Enter 'hallway' or 'search_dining_room'")
    x = room_clear.get("dining_room")
    response = input("What do you do? ")
    if response == "search_dining_room" and x == "false":
        search_dining_room()
    if response == "search_dining_room" and x == "true":
        print("You have already searched outside.")
        searched_dining_room()
    elif response == "search_dining_room":
        search_dining_room()
    else:
        print("Invalid response")
        dining_room()
def searched_dining_room():
    print("dining_room. Enter 'hallway' or 'search_dining_room'")
    x = room_clear.get("dining_room")
    response = input("What do you do? ")
    if response == "hallway":
        hallway()
    if response == "search_dining_room" and x == "true":
        print("This place has already been searched.")
        searched_dining_room()
    else:
        print("Invalid response")
        searched_dining_room()
def search_dining_room():
    print("Search dining room")
    challenge_completed()
    room_clear.update({"dining_room": "true"})
    searched_dining_room()


def kitchen():
    print("kitchen. Enter'hallway' or 'search_kitchen'")
    x = room_clear.get("kitchen")
    response = input("What do you do? ")
    if response == "search_kitchen" and x == "false":
        search_kitchen()
    if response == "search_kitchen" and x == "true":
        print("You have already searched this room.")
        searched_kitchen()
    elif response == "hallway":
        hallway()
    else:
        print("Invalid response")
        kitchen()
def searched_kitchen():
    print("kitchen. Enter 'hallway' or 'search_kitchen'")
    x = room_clear.get("kitchen")
    response = input("What do you do? ")
    if response == "hallway":
        hallway()
    if response == "search_kitchen" and x == "true":
        print("This room has already been searched.")
        searched_kitchen()
    else:
        print("Invalid response")
        searched_kitchen()
def search_kitchen():
    print("Search kitchen")
    challenge_completed()
    room_clear.update({"kitchen": "true"})
    searched_kitchen()


def garage():
    print("garage. Enter 'hallway' or 'search_garage'")
    x = room_clear.get("garage")
    response = input("What do you do? ")
    if response == "search_garage" and x == "false":
        search_garage()
    if response == "search_garage" and x == "true":
        print("You have already searched this room.")
        searched_garage()
    elif response == "hallway":
        hallway()
    else:
        print("Invalid response")
        garage()
def searched_garage():
    print("garage. Enter 'hallway' or 'search_garage'")
    x = room_clear.get("garage")
    response = input("What do you do? ")
    if response == "hallway":
        hallway()
    elif response == "search_garage" and x == "true":
        print("This room has already been searched.")
        searched_kitchen()
    else:
        print("Invalid response")
        searched_garage()
def search_garage():
    print("Search garage")
    challenge_completed()
    room_clear.update({"garage": "true"})
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
    x = room_clear.get("lounge")
    response = input("What do you do? ")
    if response == "search_lounge" and x == "false":
        search_lounge()
    if response == "search_lounge" and x == "true":
        print("You have already searched this room.")
        searched_lounge()
    elif response == "hallway":
        hallway()
    else:
        print("Invalid response")
        lounge()
def searched_lounge():
    print("lounge. Enter 'hallway' or 'search_lounge'")
    x = room_clear.get("lounge")
    response = input("What do you do? ")
    if response == "hallway":
        hallway()
    elif response == "search_lounge" and x == "true":
        print("This room has already been searched.")
        searched_lounge()
    else:
        print("Invalid response")
        searched_lounge()
def search_lounge():
    print("Search lounge")
    challenge_completed()
    room_clear.update({"lounge": "true"})
    searched_lounge()
lounge()
