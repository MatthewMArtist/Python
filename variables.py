#name = input("What is your name?: ")
#Class = input("What is your class (Fighter, Barbarian, Rogue, wizard, Bard):")
#print("Your name is " + name)
#print("your are a " + Class)

my_name = "Matthew"
my_age = "28"
breakfast = "Cocopops"
drink = "water"
drink_reason = "refreshing"

print(my_name)
print(my_age)
print(breakfast)

breakfast = "Cheese bagels"

print(breakfast)

favourite_drink = "My favourite drink is {} Becasue it is {}.".format(drink,drink_reason)

drink = "lemonade"
print(favourite_drink)

favourite_drink = "My favourite drink is {} Becasue it is {}.".format(drink,drink_reason)
print(favourite_drink)

i = 1
print(i)
#(making the variable 'i' equal one)

i += 1
print(i)
#(adding 1 to the variable 'i')

i *= 2
print(i)
#(multiplying the variable 'i' by 2)

i /= 2
print(i)
#(dividing the variable 'i' by 2)

i -= 1
print(i)
#(subtracting 1 from the variable 'i')

age = input("what is your age?: ")
name = input("what is your name?: ")
birth_date = 2020 - int(age)
print("{} is {} years old and was born in {}.".format(name,age,birth_date))

space1 = "0"
space2 = "0"
space3 = "0"
space4 = "x"
space5 = "x"
space6 = " "
space7 = "0"
space8 = " "
space9 = " "

print("   |   |   ")
print(" {} | {} | {} ".format(space1,space2,space3))
print("   |   |   ")
print("-----------")
print("   |   |   ")
print(" {} | {} | {} ".format(space4,space5,space6))
print("   |   |   ")
print("-----------")
print("   |   |   ")
print(" {} | {} | {} ".format(space7,space8,space9))
print("   |   |   ")

#Cross win conditions:
if space1 == "x" and space2 == "x" and space3 == "x":
    print("crosses win")
if space4 == "x" and space5 == "x" and space6 == "x":
    print("crosses win")
if space7 == "x" and space8 == "x" and space9 == "x":
    print("crosses win")

if space1 == "x" and space4 == "x" and space7 == "x":
    print("crosses win")
if space2 == "x" and space5 == "x" and space8 == "x":
    print("crosses win")
if space3 == "x" and space6 == "x" and space9 == "x":
    print("crosses win")

if space1 == "x" and space5 == "x" and space9 == "x":
    print("crosses win")
if space3 == "x" and space5 == "x" and space7 == "x":
    print("crosses win")

#Naught win conditions
if space1 == "0" and space2 == "0" and space3 == "0":
    print("Naughts win")
if space4 == "0" and space5 == "0" and space6 == "0":
    print("Naughts win")
if space7 == "0" and space8 == "0" and space9 == "0":
    print("Naughts win")

if space1 == "0" and space4 == "0" and space7 == "0":
    print("Naughts win")
if space2 == "0" and space5 == "0" and space8 == "0":
    print("Naughts win")
if space3 == "0" and space6 == "0" and space9 == "0":
    print("Naughts win")

if space1 == "0" and space5 == "0" and space9 == "0":
    print("Naughts win")
if space3 == "0" and space5 == "0" and space7 == "0":
    print("Naughts win")

