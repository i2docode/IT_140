#!/usr/bin/python3
"""
Use input() to read a string from input into variable person_name. 
Then, use int(input()) to read a value from input as an integer 
into variable person_age.
"""
person_name = input('enter a name:')
person_age = int(input('enter a number:'))
print(f'In 5 years {person_name} will be {person_age + 5}')
print()


"""
Write two statements to read in values for my_city followed by my_state. 
Do not provide a prompt. Assign log_entry with current_time, my_city, and my_state. 
Values should be separated by a space.
"""

current_time = '2014-07-26 02:12:18:'
my_city = input('enter a city:')
my_state = input('enter a state:')
log_entry = current_time + ' ' + my_city + ' ' + my_state
print(log_entry)


