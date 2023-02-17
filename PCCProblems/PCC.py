# Practice Problems
"""
What do I know how to do?
I can assign a variable
I can print, add, concatenate and manage that variable
I can ask user for input, with a try and exception block to filter out data that I dont want
I can store that variable in a list or a dictionary
I can loop through a list to find the sum, average, or length of that list
    I can also loop through key, value pairs in a dictionary
I can implement logic through if else elif statements
I can interact with data from the web with an import module

How can I use some of these to create something that I can actually use??
Some beginner projects I can make:
    budgeting program, very limited im sure
    text-based game, with rooms that will kill you with conditionals
    a program that reads a file within the same directory
        potentially does some loop to manipulate the data

"""
import time

# Text-based Adventure! The goal is to create three paths where the user might gain or lose health
# They must survive until the end
# Get Name
player = input('NAME PLEASE: ')
player_stats = {'health': 100, 'attack': 100}
# Introduce to game

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
time.sleep(1.5)
door_choice = input("Before you lies TWO doors. One on your left, the other on your right. "
                    "One door may kill you. Which do you choose?\n")
if door_choice.lower() == 'left':
    player_stats['health'] = 125
    print("You have chosen correctly and are justly rewarded. Enjoy a back rub. Bolstering your health to\n"
          "brave the path ahead.")
elif door_choice.lower() == 'right':
    player_stats['health'] = 25
    print("You open the door to the sudden horror of a thousand eyes staring back at you. The foul stench\n"
          "surrounds you, suffocating your senses.")


