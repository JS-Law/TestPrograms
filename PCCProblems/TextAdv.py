import time
import random

# Objects
player = input('NAME PLEASE: ')
player_stats = {'health': 100, 'attack': 100}
inventory_list = {}


# Dice Roll
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
    print("\n")
    time.sleep(1.3)
    return dice_sum, dice_list


# Scenes
def intro():
    print('Welcome to the show, ' + player.title() + '!')
    time.sleep(1)
    print("Only one path lies before you. A long hallway with many doors, filled with malice and malcontent")
    time.sleep(1)
    answer = None
    while answer not in ("yes", "no"):
        answer = input('Do you, ' + player.title() + ', wish to proceed?\n')
        time.sleep(1.3)
        if answer == "yes":
            print('I was hoping you would say that..\n')
            time.sleep(.8)
            first_scene()
            break
        elif answer == "no":
            print("Fine, " + player.upper() + ", no ice cream for you.")
            quit()
        else:
            print("Please enter yes or no.")


def first_scene():
    door1_choice = None
    directions = ['left', 'right']
    while door1_choice not in directions:
        door1_choice = input("Before you lies TWO doors. One on your left, the other on your right. "
                             "One door may kill you. Which do you choose?\n")
        if door1_choice.lower() == 'left':  # 'Correct' choice.
            player_stats['health'] = player_stats['health'] + 25
            print("You have chosen correctly and are justly rewarded.\n Enjoy a back rub. Bolstering your health to\n"
                  "brave the path ahead.")
            time.sleep(2)
            second_scene()
        elif door1_choice.lower() == 'right':  # 'Incorrect' choice.
            player_stats['health'] = player_stats['health'] - 75
            print("You open the door to the sudden horror of a thousand eyes staring back at you. The foul stench\n"
                  "surrounds you, suffocating your senses. Rendering you incapacitated.")
            time.sleep(1.2)
            print("You awaken back in the hallway to the sound of dice, tumbling within a small velvet bag")
            time.sleep(.3)
            bonus_roll = input("Do you wish to roll?\n")
            # Bonus Roll For Extra Health!
            if bonus_roll == 'yes':
                bonus_dice_roll = diceroll()
                print(bonus_dice_roll)
                current_roll = bonus_dice_roll[0]
                player_stats['health'] = player_stats['health'] + current_roll
                second_scene()
                if bonus_dice_roll[0] >= 36:
                    print("Congrats! You've won!")
                    quit()
                    player_stats['life'] = 1


def second_scene():
    print("You see a silhouette of a person further down the hall way")
    time.sleep(1)
    answer = None
    while answer not in ("yes", "no"):
        answer = input("Do you wish to pursue?\n")
        time.sleep(.6)
        if answer == "yes":
            print("You take off after the figure and find yourself in an open room with many decisions.")
            time.sleep(1.6)
            print("...and even more questions.")
            third_scene()
            break
        elif answer == "no":
            print("Your inaction has cost you your life, please try again next time.")
            quit()
        else:
            print("Please enter yes or no.")


# Chamber Scene 
def third_scene():
    wind_sound = "BwooOOooOOooooOOooOOooooOOooOOooooOOooOOooooOOooOOoosh\n"
    for i in wind_sound:
        time.sleep(.15)
        print(i, end="")
    print("A light from above descends from the center of the room, illuminating your surrounding area")
    time.sleep(.15)
    print("before bleeding into darkness..")
    choice = None
    directions = ['left', 'right', 'backward', 'forward']
    while choice not in directions:
        choice = input("Choose your path: Forward, Backward, Left, Right\n")
        if choice == 'left':
            print('nice')
            # item
        elif choice == 'right':
            print('nice')
            # mob
        elif choice == 'forward':
            print('nice')
            # dice game loss health
        elif choice == 'backward':
            print('nice')
            # lose health
        else:
            continue


intro()
print(player_stats)
