import random


#
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


x = diceroll()
print(x[0])

