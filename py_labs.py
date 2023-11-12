#!/usr/bin/python3
import math
# program that finds the smallest of 3 integers or floats when input.
# checks for both negative numbers and positive integers or floats.

# int0 = int(input())
# int1 = int(input())
# int2 = int(input())

# def smallest_number(int0, int1, int2):
#     num_list = []
#     num_list.append(int0)
#     num_list.append(int1)
#     num_list.append(int2)

#     for n in range(len(num_list)):
#         if num_list[n] < int1 and n < int2:
#             return n
        
#         elif num_list[n] < int0 and n < int2:
#             return n
        
#         elif num_list[n] < int0 and n < int1:
#             return n
        
#         else:

#             return 'ivalid input'

        

        




# target_int = smallest_number(int0, int1, int2)
# print(target_int)

# # c&p
# if (int0 < int2 and int0 < int2):
#     smallest = int0

# elif (int1 < int0 and int1 < int2):
#     smallest = int1

# else:
#     smallest = int2


# month = input()
# day = int(input())
# if month in ('April', 'May'):
#     print('Spring')
# elif month in ('June','July', 'August'):
#     print('Summer')
# elif month in ('October', 'November'):
#     print('Autumn')
# elif month in ('January', 'March'):
#     print("Winter")
# elif month == 'June' and (day == range(1, 20)):
#     print("Spring")

# elif month == 'June' and (day == range(21, 30)):
#     print("Summer")
# elif month == 'September' and (day == range(1, 21)):
#     print("Summer")
# elif month == 'September' and (day == range(22, 30)):
#     print("Autumn")
# elif month == 'December' and (day == range(1, 20)):
#     print("Autumn")
# elif month == 'December' and (day == range(21, 31)):
#     print("Winter")
# elif month == 'March' and (day == range(1, 19)):
#     print("Winter")

# elif month == 'March' and (day == range(20, 31)):
#     print("Spring")


# elif month == 'February' and (day == range(1, 28)):
#     print("Winter")
# else:
#     print("Invalid")

overtime = int(input('total hours of overtime: '))

hr_rate = 20
hours_per_week = 40
ot_rate = 30
net_per_week = hr_rate * hours_per_week 
adjusted_net = net_per_week + (ot_rate * overtime)
print(adjusted_net, '\n')

# user defined functions
    # function; named series of statements.


def test_fun():
    test_itr_list = [
        'test itr a', 
        'test itr b', 
        'test itr c'
    ]
    for itr in range(len(test_itr_list)):
        print(test_itr_list[itr])
test_fun()


# function parameters & arguments
# A parameter is a function input 
    # specified in a function definition. 
    # ex: iterating function may have a list as input.

# An argument is a value provided to a function's parameter during a function call.
    # is a value provided to a function's parameter during a function call.
        # ex: iterate_list([0, 1, 2, 3, 4, 5])

# function that is called twice
def print_num(num):
    print(num  / 2)
print_num(19)




# multiple paramters
# functions can have multiple parameters
# arguments are assigned to parameters by position.
def print_sum(num1, num2, x):
    # callback function  applied here?
    print(num1, '+', num2, 'is', (num1 + num2))
    print(x + 400)
print_sum(1, 2, 99)

def output_data_fun(out_data):
    print(in_data + 10)
in_data = int(input('enter an integer: '))
output_data_fun(in_data)

# return values from functions
def square_root(x):
    return math.sqrt(x)
y = round(square_root(49.9))
# final return statement, output.
z = y
print(z)

# mathematical functions

input_str = input()
target_character = input_str[0]
print(target_character)

phrase_str = input_str[1:]
print(phrase_str)

count_char = phrase_str.count(target_character)
print(count_char)















        


    
    







                











