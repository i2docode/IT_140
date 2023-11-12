#!/usr/bin/python3
import math
from collections import namedtuple
print('python test output')

# prints new-line.
print()

# statement that outputs code on the same line without defaulting to a new line.
print('python3 code', end=' ')

# multi-lined string
figure = """*****
*   *
*****
*   *
*****"""
print(figure)

# output variable value.
code_lang = '\npython programming'
print(code_lang)

"""
outputting multiple items with one statement;
print('string', variable, 1)
"""
engineer_type = 'firmware engineer'
degree = 'computer science - software engineering'
print(degree, engineer_type)

# python 1.4 error debugging
"""
syntax error.
test_var0 = True
print('Test variable:' test_var0)
"""
test_var0 = True
print(f'\nTest variable:{test_var0}')

# variables with assignments on the left and right.
user_num = 1
user_num2 = 3
neg_user_nums_diff = user_num - user_num2
print(f'{user_num} - {user_num2} equals > {neg_user_nums_diff}')

"""
numeric types; floating point number.
the decimal can show up/float to any point in the number.

A floating-point literal is written with the fractional part 
even if that fraction is 0, as in 1.0, 0.0, or 99.0.
"""

print(float(1.0e-4))
print(float(7.2e-4))

"""
python strings - sequence of indexed characters
enclosed within single or doubled quotation marks.

python string characters cannot be modified
must update the variable by assign a whole new value.

# prohibited
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# Change to upper case

alphabet[0] = 'A'  # Invalid: Cannot change character
alphabet[1] = 'B'  # Invalid: Cannot change character

print('Alphabet:', alphabet)
"""
test_str = 'python software engineering'
test_str = 'python software development'
print(test_str)
print()


"""
python lists
data structure/container that stores indexed data types & data structures.
booleans, integers, strings, lists, objects, tuples

array elements can be reassigned.

accessing list elements
use bracket notation.

adding elements to a list.
list_name.append()

removing elements from a list.
.pop() default removes the last element at index i from list.
also removes the provided argument from a list.
list_name.pop()

.remove(arg) removes the first element from a list that matches the agument.
list_name.remove(arg)
"""
test_list = [0, 1, 2, 3, 4, 5, 6, 7]
test_list[1] = 'ab'
print(test_list)




"""
Sequence-type functions are built-in functions that operate on 
sequences like lists and strings. Sequence-type methods are methods 
built into the class definitions of sequences like lists and strings.

"""






"""
*python dictionaries.
made up of key-value pairs.

It provides us with a way to 
map pieces of data to each other 
so that we can quickly find values 
that are associated with one another.

*dictionaries need hashable keys;
values that cannot be changed > numbers and strings.

*can declare an empty dictionary.
empty_dict = {}


*adding keys
dictionary[new_key] = 'new key value'

*adding multiple keys
dictionary.update({

})

"""

dict_0 = {
    'bool':True,
    0:False
}
print(dict_0)

# iterate through first dictionary and add key-vals to the second based on iterated key-values.
dict_1 = {}


x = 2.3
z = math.ceil(x)
print(z)
print()
z = math.floor(x)
print(z)


z = 4.5
z = math.pow(math.floor(z), 2.0)
print(z)

z = 4
z = math.factorial(z)
print(z)

"""
lists - data structure/object/way of 
organizing different python data types.

can store nested lists within a list.

list operations

len(list)	Find the length of the list.
list1 + list2	Produce a new list by concatenating list2 to the end of list1.
min(list)	Find the element in list with the smallest value.
max(list)	Find the element in list with the largest value.
sum(list)	Find the sum of all elements of a list (numbers only).
list.index(val)	Find the index of the first element in list whose value matches val.
list.count(val)	Count the number of occurrences of the value val in list.
list.pop(val)/list.pop() - removes an indexed item from a list, removes last element 
from a list by default.
list.append(element) - adds an element to the end of a list. adds list to end 
of a list as a nested list.
"""
test_list = [0, 1, 2, 3]
new_test_list = [0]
test_list.append(new_test_list)
print(test_list)

"""
tuples - ordered/indexed data structure 
where elements are immutable/cannot change.

supports len() indexing, and other sequence type functions.
"""

"""
Let Address = namedtuple('Address', ['street', 'city', 'country']). 

Create a new address object house where house.street is "221B Baker Street", 
house.city is "London", and house.country is "England".
"""

Address = namedtuple('Address', ['street', 'city', 'country'])

house = Address("221B Baker Street", "London", "England")
print(house.street)

"""
    Common formatting specification presentation types.

    Type	Description	Example	Output
    s	String (default presentation type - can be omitted)	'{:s}'.format('Aiden') Aiden

    d	Decimal (integer values only) '{:d}'.format(4) 4

    b	Binary (integer values only) '{:b}'.format(4) 100

    x, X	Hexadecimal in lowercase (x) and uppercase (X) (integer values only) '{:x}'.format(15) f

    e	Exponent notation	'{:e}'.format(44) 4.400000e+01

    f	Fixed-point notation (6 places of precision) '{:f}'.format(4) 4.000000

    .[precision]f	Fixed-point notation (programmer-defined precision) '{:.2f}'.format(4) 4.00


Referencing the correct format() values in replacement fields.

Inferred positional replacement	'{:s} ${:.2f} tacos is ${:.2f} total'.format('Three', 1.50, 4.50)

Three $1.50 tacos is $4.50 total



Positional replacement

'{0:s} ${2:.2f} tacos is ${1:.2f} total'.format('Three', 4.50, 1.50)

Three $1.50 tacos is $4.50 total



Named replacement	

'{cnt:s} ${cost:.2f} tacos is ${sum:.2f} total'.format(cnt = 'Three', cost = 1.50, sum = 4.50)

Three $1.50 tacos is $4.50 total

"""

"""
If num_people is greater than 10, execute group_size = 2 * group_size. 
Otherwise, execute group_size = 3 * group_size 
and num_people = num_people - 1.
"""

num_people = 10
group_size = 5
if num_people > 10:
    group_size = 2 * group_size
    print(group_size)
else:
    group_size = 3 * group_size
    print(group_size)
num_people = num_people - 1
print(num_people)

"""
If num_players is greater than 11, execute team_size = 11. Otherwise, 
execute team_size = num_players. Then, no matter the value of num_players,
execute team_size = 2 * team_size.
"""

num_players = 15
if num_players > 11:
    team_size = 11
else:
    team_size = num_players
team_size = 2 * team_size

name = 'aaron'

code_lang = 'python'

my_output = f'my name is {name}, and I love to code in {code_lang}.'

print(my_output)

"""
Write an if-else statement with multiple branches.

If year is 2101 or later, print "Distant future" (without quotes). 

Otherwise, if year is 2001 or greater, print "21st century". 

Otherwise, if year is 1901 or greater, print "20th century". 

Else (1900 or earlier), print "Long ago".
"""
year = 1776

if year >= 2101:
    print('Distant future')
elif year >= 2001:
    print("21st century")
elif year >= 1901:
    print('20th century')
else:
    print('Long ago')


sales_type = 1
sales_bonus = 0

sales_type = 2
sales_bonus = 4

sales_type = 2
sales_bonus = 7

if sales_type == 2:
   if sales_bonus < 5:
      sales_bonus = 10
   else:
      sales_bonus = sales_bonus + 2

else:
   sales_bonus = sales_bonus + 1
print(sales_bonus)

# multiple distinct if statements - statements are independent of eachother.
num_boxes  = 0
num_apples = 9 

if num_apples < 20:
   num_boxes = 3
   print(num_boxes)

if num_apples < 10:
   num_boxes = num_boxes - 1
   print(num_boxes)


num_boxes  = 0
num_apples = 9 

if num_apples < 10:
   if num_apples < 5:
      num_boxes = 1
   else: 
      num_boxes = 2
elif num_apples < 20:
   num_boxes = num_boxes + 1
print(num_boxes)

"""
Write multiple if statements. 

If car_year is 1969 or earlier, print "Few safety features." 

If 1970 or later, print "Probably has seat belts." 

If 1990 or later, print "Probably has antilock brakes." 

If 2000 or later, print "Probably has airbags." 

End each phrase with a period '.'
"""
car_year = 1995

if car_year <= 1969:
   print('Few safety features.')

if car_year >= 1970:
   print("Probably has seat belts.")

if car_year >= 1990:
   print("Probably has antilock brakes.")

if car_year >= 2000:
   print('Probably has airbags.')
   
"""
equality and relational operators


"""































