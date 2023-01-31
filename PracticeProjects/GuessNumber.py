import random


def guess(x):
    random_number = random.randint(1, x)  # assigns the random number w/ the import, the arg means random from 1 thru x
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry , Guess Higher!')
        elif guess > random_number:
            print('Sorry , Guess again(lower)')

    print('Hell Yeah, you guessed it!!!!!!!!!!!!!!!!')


guess(50)
