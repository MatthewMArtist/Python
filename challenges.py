#Challenge 1: 
#Create a variable called password. Check how many letters are in the password, if there are less than 8 print that the password is too short. Otherwise print the password.
#HINT: We have used a method to count the length of a string before…

password = input("password: ")
password_len = len(password)

if password_len > 7:
    print(password)
else:
    print("Your password is not long enough")

#Challenge 2: 
#Create a variable called num. Check if the variable is divisible by 3 or 5. If it is print “This number is divisible by 3 or 5”. Otherwise print “This number is not divisible by 3 or 5.”
#HINT: We do not use the divide operator, but rather one that helps us deal with no remainders (integers)

num = 3
div_num_3 = num / 3
div_num_5 = num / 5

if (div_num_3).is_integer() or (div_num_5).is_integer():
    print("This number is divisible by three")
else:
    print("This number is not divisible by three")

#Challenge 3: 
#Create a variable called num. If num is divisible by 3 print “fizz”, if it’s divisible by 5 print “buzz”, if it’s divisible by both 3 and 5 print “fizz buzz”. Otherwise print num.
#HINT: See hint to challenge 2, but think about the structure of your if statement as well…

num = 5
div_num_3 = num / 3
div_num_5 = num / 5

if (div_num_3).is_integer() and (div_num_5).is_integer():
    print("Fizz buzz")
else:
    if (div_num_3).is_integer():
        print("Fizz")
    if (div_num_5).is_integer():
        print("Buzz")

if div_num_3%1 != 0 and div_num_5%1 != 0:
    print(num)

# Challenge 4:
# Create a variable called num. Check if the number is a palindrome (looks the same forward as it does backwards e.g. 1001 or 20202).
# HINT: Research how we can do this, pay close attention to index position. We will use it differently to how we have up until now.

num = "101"

num = num.casefold()

rev_num = reversed(num)

if list(num) == list(rev_num):
    print("This number is palindrome")
else:
    print("this number is not palindrome")

# Challenge 5: 
# Create a variable called time, a variable called place_of_work and a variable called town_of_home. Create an if statement that prints where someone is at times of the day. E.g. if the time is 7 I’m at home, at 8 I’m commuting, at 9 I’m at work.
# HINT: This one is fairly open ended and seems straight forward. If you find it easy, see how you can improve it to include 24 hour clock/evenings?

# time =
# place_of_work =
# town_of_home =


# space1 = "0"
# space2 = "0"
# space3 = "0"
# space4 = "x"
# space5 = "x"
# space6 = " "
# space7 = "0"
# space8 = " "
# space9 = " "

# print("   |   |   ")
# print(" {} | {} | {} ".format(space1,space2,space3))
# print("   |   |   ")
# print("-----------")
# print("   |   |   ")
# print(" {} | {} | {} ".format(space4,space5,space6))
# print("   |   |   ")
# print("-----------")
# print("   |   |   ")
# print(" {} | {} | {} ".format(space7,space8,space9))
# print("   |   |   ")

# #Cross win conditions:
# if space1 == "x" and space2 == "x" and space3 == "x":
#     print("crosses win")
# if space4 == "x" and space5 == "x" and space6 == "x":
#     print("crosses win")
# if space7 == "x" and space8 == "x" and space9 == "x":
#     print("crosses win")

# if space1 == "x" and space4 == "x" and space7 == "x":
#     print("crosses win")
# if space2 == "x" and space5 == "x" and space8 == "x":
#     print("crosses win")
# if space3 == "x" and space6 == "x" and space9 == "x":
#     print("crosses win")

# if space1 == "x" and space5 == "x" and space9 == "x":
#     print("crosses win")
# if space3 == "x" and space5 == "x" and space7 == "x":
#     print("crosses win")

# #Naught win conditions
# if space1 == "0" and space2 == "0" and space3 == "0":
#     print("Naughts win")
# if space4 == "0" and space5 == "0" and space6 == "0":
#     print("Naughts win")
# if space7 == "0" and space8 == "0" and space9 == "0":
#     print("Naughts win")

# if space1 == "0" and space4 == "0" and space7 == "0":
#     print("Naughts win")
# if space2 == "0" and space5 == "0" and space8 == "0":
#     print("Naughts win")
# if space3 == "0" and space6 == "0" and space9 == "0":
#     print("Naughts win")

# if space1 == "0" and space5 == "0" and space9 == "0":
#     print("Naughts win")
# if space3 == "0" and space5 == "0" and space7 == "0":
#     print("Naughts win")


age = input("What is your age?: ")
age = int(age)
if age < 18:
    print("The price of admission is £8.")
if age >= 18 and age < 60:
    print("the price of admission is £10.95.")
if age >= 60:
    print("the price of admission is £7.50.")


