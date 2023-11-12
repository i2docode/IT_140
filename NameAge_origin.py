#!/usr/bin/python3
name_input = input('What is your name? ')
age_input = int(input('How old are you? '))
current_year = 2023
calc_user_birth_year = current_year - age_input
message = 'Hello {}! You were born in {}.'.format(name_input, calc_user_birth_year)
print(message)



