# favourite_songs = [
#     "Resonance",
#     "To the abyss",
#     "Midnight city"
# ]

# print(favourite_songs)

# favourite_songs[1] = "Oni"

# print(favourite_songs)
# print(len(favourite_songs))

# favourite_songs.append("Oni")
# print(favourite_songs)

# favourite_songs.pop()
# print(favourite_songs)

favourite_websites = [
    "Youtube",
    "Spacebattles",
    "AIdungeon"
]
other_websites = [
    "Google",
    "Sufficient velocity"
]
favourite_websites.remove("Youtube")
print(favourite_websites)

favourite_websites.append("Youtube")
print(favourite_websites)

favourite_websites.reverse()
print(favourite_websites)

favourite_websites.sort()
print(favourite_websites)

print(favourite_websites.count("Youtube"))

favourite_websites.extend(other_websites)
print(favourite_websites)

favourite_websites.insert(2,"Discord")
print(favourite_websites)

favourite_websites.clear()
print(favourite_websites)


def sandwitch(topping1,topping2,topping3,topping4,topping5):
    print("your sandwitch contains {}, {}, {}, {} and {}.".format(topping1,topping2,topping3,topping4,topping5))

sandwitch("ketchup","cheese","lettuce","ham","butter")

list = [
    "part1",
    "part2",
    "part3"
]
print(list)

list.insert(0,"part4")
print(list)

for lis in list:
    print(lis)

# i = 1

# for i in range(10):
#     print(1)

# import random

# for i in range(10):
#     print(random.randint(1,100))

for i in range(9,-1,-1):
    print(i)

def film_check():
    if favourite_films.index("ghostbusters") == 2:
        print("Yes it's ghostbusters")
    else:
        print("booo, we want ghostbusters!")

favourite_films = [
    "Your name",
    "The thing",
    "ghostbusters",
    "Alien"
]

favourite_films.append("Broly movie")
favourite_films.append("Broly movie dbs")

for loop in favourite_films:
    print(loop)

film_check()



