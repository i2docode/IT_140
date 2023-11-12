#!/usr/bin/python3
# basic output with variables
print()
"""
Enter integer:
4
You entered: 4
4 squared is 16 
And 4 cubed is 64 !!
Enter another integer:
5
4 + 5 is 9
4 * 5 is 20
"""
user_num = int(input('Enter integer:\n'))
print(user_num)
print(f'You entered: {user_num}')
print(f'{user_num} squared is {user_num * user_num}')
print(f'And {user_num} cubed is {user_num * user_num * user_num} !!')
user_num2 = int(input('Enter a second integer:\n'))
print(user_num2)
print(f'{user_num} + {user_num2} is {user_num + user_num2}')
print(f'{user_num} * {user_num2} is {user_num * user_num2}\n')


print()
#

