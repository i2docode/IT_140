#!/usr/bin/python3
user_full_name = input()
user_full_name = user_full_name.split()

if len(user_full_name) == 2:
    first_name = user_full_name[0]
    last_name = user_full_name[1]
    print('{}, {}.'.format(last_name, first_name[0]))

elif len(user_full_name) == 3:
    first_name = user_full_name[0]
    middle_name = user_full_name[1]
    last_name = user_full_name[2]
    print('{}, {}.{}.'.format(last_name, first_name[0], middle_name[0]))
else:
    print("Invalid input")

# dict_obj = { 'key_0':['a', 0, 'b', 1], 'key_1':['c', 2, 'd', 3] }
# print(dict_obj['key_0'][0])
# print(dict_obj['key_1'][0])
# dict_obj['key_0'][0] = 'A'
# print(dict_obj['key_0'][0])
