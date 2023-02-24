import time
import random

# Objects
player = input('NAME PLEASE: ')
player_stats = {'health': 100, 'attack': 100}
inventory_list = {}


def printer(message):
    for i in message:
        time.sleep(.15)
        print(i, end="")


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
            print("You have chosen correctly and are justly rewarded.")
            time.sleep(1)
            print("You have gained health")
            second_scene()
        elif door1_choice.lower() == 'right':  # 'Incorrect' choice.
            player_stats['health'] = player_stats['health'] - 75
            print("You open the door to the sudden horror of a thousand eyes staring back at you.")
            time.sleep(.3)
            print("The foul stench surrounds you, suffocating your senses. Rendering you incapacitated.")
            time.sleep(1.2)
            print("You awaken back in the hallway to the sound of dice, tumbling within a small velvet bag")
            time.sleep(.3)
            bonus_roll = input("Do you wish to roll?\n")
            # Bonus Roll For Extra Health!
            if bonus_roll == 'yes':
                bonus_dice_roll = diceroll()
                # print(bonus_dice_roll)
                current_roll = bonus_dice_roll[0]
                player_stats['health'] = player_stats['health'] + current_roll
                print("Great! You've gained " + str(current_roll) + " health!")
                time.sleep(.5)
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
    wind_sound = "BwooOOooOOooooOOooOOoosh\n"
    for i in wind_sound:
        time.sleep(.15)
        print(i, end="")
    print("A light from above descends from the center of the room, illuminating your surrounding area")
    time.sleep(.15)
    print("before bleeding into darkness..")
    choice = None
    directions = ['left', 'right', 'forward']
    while choice not in directions:
        choice = input("Choose your path: Forward, Backward, Left, Right\n")
        if choice == 'left':
            left_scene()
        elif choice == 'right':
            right_scene()
        elif choice == 'forward':
            forward_scene()
            # dice game loss health
        else:
            continue


# Sixth Scene
def forward_scene():
    if 'rolled' in player_stats:
        print("Sorry, looks like you've already rolled!")
    elif 'rolled' not in player_stats:
        print("Ah, look, the dice set that restored some health earlier.")
        bonus_roll = input("Do you wish to try again?\n")
        # Bonus Roll For Extra Health!
        if bonus_roll == 'yes':
            player_stats['rolled'] = 1
            bonus_dice_roll = diceroll()
            # print(bonus_dice_roll)
            current_roll = bonus_dice_roll[0]
            player_stats['health'] = player_stats['health'] + current_roll
            print("Great! You've gained " + str(current_roll) + " health!")
            time.sleep(.5)
            third_scene()
            if bonus_dice_roll[0] >= 36:
                print("Congrats! You've won!")
                quit()
                player_stats['life'] = 1
    third_scene()


# fourth scene!
def left_scene():
    message = "You enter a small room, littered with cabinets and a few too many clocks\n"
    printer(message)
    time.sleep(.4)
    user_input = None
    while user_input not in ("yes", "no"):
        user_input = input("Would you like to take a look around?\n")
        if user_input == 'yes':
            item = "You peer around, examining the room for anything of value\n"
            printer(item)
            suspense_lol = "..."
            printer(suspense_lol)
            eureka = "Nothing too extraordinary here, you start for the door and trip and fall into\n" \
                     "the corner of the room, knocking over a small side table that revealed a sword!\n"
            printer(eureka)
            exit_room = "You exit the room."
            player_stats['attack'] = player_stats['attack'] + 100
            third_scene()
            printer(exit_room)

        elif user_input == 'no':
            message = "Are you sure?\n There could be something cool!"
            choice = input("")
            if choice == 'yes':
                message = "Suit yourself!"
                printer(message)
                third_scene()


def right_scene():
    message = "You enter the room to see two shadowy figures shuffling about, one of which hastily exits\n" \
              "to the next room.\n "
    printer(message)
    mob = "You're left face to face with a ghoul, standing 7ft tall, attack!\n"
    printer(mob)
    if player_stats['attack'] > 100:
        won = "In one swift motion, you manage to unsheathe your sword and it finds its way to the ghouls heart!\n"
        printer(won)
        won = "You plunge the sword deeper into the creatures heart and just as the hilt touches the ghouls breast\n" \
              "a golden hue emanates from the the creatures back, enveloping all but your thoughts..\n"
        printer(won)
        won = "After regaining your sight, you follow the second figure who escaped."
        printer(won)
        player_stats['attack'] = player_stats['attack'] + 100
        boss_scene()
    elif player_stats['attack'] <= 100:
        message = "You lunge for the ghoul, who strikes just as swiftly, sending you back to the hall."
        third_scene()


def boss_scene():
    if player_stats['attack'] == 300:
        message = "You see something manifest in the distance...\n" \
                  "it...\nlooks..\nLike, You!\n"
        printer(message)
        choice = None
        while choice not in ("yes", "no"):
            choice = input("Do you wish to attack?\n")
            if choice.lower() == 'yes':
                message = "Every blow, every strike you dole, mirrored by You\n" \
                          "it seems neither you nor You can be harmed by the other\n" \
                          "as your stamina begins failing, your sword begins to glow brighter and brighter..\n" \
                          "CLINK...\n" \
                          "The final blow has landed, and you claim victory! YOU WON"
                printer(message)
            if choice.lower() == 'no':
                message = "Unwise...\n" \
                          "..."
                time.sleep(3)
                message = "You...\n" \
                          "Won?\n" \
                          "You won!"
                printer(message)
                quit()
    elif player_stats['attack'] < 300:
        message = "You begin to open the door and feel a dense fog, so dense that it is impassable.\n" \
                  "Return to the hall, you may require something to preceed.."
        printer(message)
        third_scene()



intro()
print(player_stats)

"""
What a nightmare!
This is my first project after a month of learning python
Theres a whole lot I could have altered on the fly but this was a very good learning experience.
I want to keep this version to use as comparison for future projects.
Things I Could Have Changed:
    Nested entire game within a while loop to create global commands
    I could have relaxed a bit on the narration and relied more upon player experience to dictate story.
        -i.e. create stats/choices/inventory and let the player wander through the level 'freely'
        instead of managing those decisions based off of conditional statements like I had
    I guarantee there are DOZENS of lines of code I could have elimated as well
    Some lines I already laugh at

"""