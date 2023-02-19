import random
import time

# Dice Roll Function
"""

def diceroll():
    dice_sum = 0
    dice_list = []
    for i in range(6):
        rand_int = random.randint(1, 6)
        dice_list.append(rand_int)
        # print(rand_int)
        # print(dice_list)
    for num in dice_list:
        dice_sum = dice_sum + num
    print("You have rolled\n" + str(dice_list) + "\nWith a sum of: " + str(dice_sum))
    return dice_sum, dice_list  # Returns

def intro():
    print('Welcome to the show, ' + player.title() + '!')
    time.sleep(2)
    print("Only one path lies before you. A long hallway with many doors, filled with malice and malcontent")
    time.sleep(1.5)
    answer = None
    while answer not in ("yes", "no"):
        answer = input('Do you, ' + player.title() + ', wish to proceed?\n')
        time.sleep(1.3)
        if answer == "yes":
            print('I was hoping you would say that.')
            break
        elif answer == "no":
            print("Fine, " + player.upper() + ", no ice cream for you.")
            quit()
        else:
            print("Please enter yes or no.")
            
x = diceroll()
print(x[0])
"""
# I need to figure out how to nest the entire game within a while loop in order to validate certain inputs that
# call certain functions depending on the input received

# Inventory function


# Function Scenes
# Intro

# loop that iterates over a string and prints on the same line
# lets try to make this a function tomorrow!
string = input("Please Enter Your Name: ")
message = "hello " + string
for i in message:
    time.sleep(.19)
    print(i,end="")


