#!/usr/bin/python3
word0 = input()
word1 = input()
num = int(input())

print(f'You entered: {word0} {word1} {num}\n')

first_passwd = f'{word0}_{word1}'
second_passwd = f'{num}{word0}{num}'

print(f'First password: {first_passwd}')
print(f'Second password: {second_passwd}\n')

first_passwd_count = len(first_passwd)
second_passwd_count = len(second_passwd)

print(f'Number of characters in {first_passwd}: {first_passwd_count}')
print(f'Number of characters in {second_passwd}: {second_passwd_count}')
