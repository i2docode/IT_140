#!/usr/bin/python3
import random

initialize_game = input('would you like to play a game?: ')

confirm_phrases = ['sure', 'ok', 'yes', 'y', 'lets play', 'game on!']

for phrase in confirm_phrases:

    if initialize_game in confirm_phrases:

        lower_bound = int(input('great! now enter lower bound number: '))

        upper_bound = int(input('sweet! now enter a upper bound number: '))

        # variable that sets the random number to be guessed.
        rando_int = random.randint(lower_bound, upper_bound)

        # variable that prompts user to enter an integer guess.
        user_guess = int(input(f'ok, now guess the number between {str(lower_bound)} and {str(upper_bound)}: '))

        # utilize while loop to run until clause become false.
        # checks if user guess is greater than random integer.
        while True:
            # checks if user guessis lower than random int.
            if user_guess < rando_int:

                # user is prompted to guess another number.
                user_guess = int(input('Nope too low. '))

                # continue statement initializes while loop.
                continue

            # checks if user guess is higher that random int.
            elif user_guess > rando_int:
                # user is prompted to guess another number.
                user_guess = int(input('Nope too high. '))
                # continue statement initializes while loop.
                continue

            # else statemen confirms correct number/
            else:
                # winnner output message.
                print('You got it!')

                break
    else:

        print('ok, have a great day... Goodbye!!')

        exit()





    

            








