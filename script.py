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

checks whether two operands' values are the same (==) or different (!=).

an expression involving an equality operator evaluates to a Boolean value. 

A Boolean is a type that has just two values: True or False.
"""
x = True
y = False
z = x

print(x == y)
print(x == z)
print(y == z)

print(x != z)
print(x != y)
print(z != y)

"""
relational operators check how one operand's value relates to another, like being greater than.

Some operators, like >=, involve two characters. 

A programmer cannot arbitrarily combine the >, =, and < symbols; only the shown two-character sequences represent valid operators.
"""

"""
operator chaining - comparing multiple values, using multiple
comparison operators in one expression.
"""

num_items = 3
if num_items == 3:
   num_items = num_items + 1
print(num_items)

num_items = 3

"""
if num_items > 10:
   num_items = num_items + 1
print(num_items)

syntax error
"""

if num_items > 10:
   num_items = num_items + 1
print(num_items)

"""
boolean refers to a value that is either
True or False.

boolean operator treats operands
as True or false and evaluates to a
value of True or False.

boolean operators include and, or, not.

boolean expression is an expression using
boolean operators.
"""

val_a = 1
val_b = ''
if val_a and val_b:
   print('both truthy')
else:
   print('both not truthy')

"""
membership and identity operators: in/not in

in and not in operators, known as membership operators, yield True or False 
if the left operand matches the value of some element in the right 
operand, which is always a container.

identity operators: is/is not

use the identity operator, is, to check whether two operands are bound to a single object. 
The inverse identity operator, is not, gives the negated value of 'is'.

The id() function can be used to retrieve the identifier of any object.
"""



"""
Problem: A company wants a program that will calculate the weekly paycheck for an employee 

based on how many hours they worked. For this company, an employee earns $20 an hour for the

first 40 hours that they work.The employee earns overtime, $30 an hour, 

for each hour they work above 40 hours.

Example: If an employee works 60 hours in a week, they would earn $20/hr for the first 40 hours. 

Then they would earn $30/hr for the 20 hours they worked overtime. 

Therefore, they earned: ($20/hr * 40hrs) + ($30/hr * 20 hrs) = $800 + $600 = $1400 total.


employee_rate = 20

employee_hours = 40

overtime_rate = 30

overtime_hours = int input()

paycheck = employee_rate * employee_hours


IF overtime_hours > 0  THEN 

	paycheck += (overtime_rate * overtime_hours )
	
	PRINT paycheck

ENDIF

EISE 
	PRINT paycheck

"""

employee_rate = 20

employee_hours = 40

overtime_rate = 30

overtime_hours = int(input('employee overtime hours: '))

paycheck = employee_rate * employee_hours

if overtime_hours > 0:
    paycheck += (overtime_hours * overtime_rate)
    print(paycheck)
else:
    print(paycheck)


"""
Write a program whose inputs are three integers, 
and whose output is the smallest of the three values.
"""

input_val_0 = 1
input_val_1 = -1
input_val_2 = 4

if input_val_0 < input_val_1 and input_val_0 < input_val_2:
    print(input_val_0)
elif input_val_0 > input_val_1 and input_val_2 > input_val_1:
    print(input_val_1)
else:
    print(input_val_2)



"""
Write a program that takes a date as input and outputs the date's season. 
The input is a string to represent the month and an int to represent the day.
"""

month = input()
day = int(input())
year_months = ('January', 'February','March', 'April' , 'May' , 'June' , 'July' , 
'August' , 'September' , "October" , "November" , "December")

if not(month in year_months ):
    print("Invalid")

elif month == 'March':
    if not(1<=day<=31):
        print ("Invalid")
    elif day<=19:
        print("Winter")
    else:
        print ("Spring")
elif month == 'April' :
    if not(1<=day<=30):
        print("Invalid")
    else:
        print("Spring")
elif month == 'May':
    if not(1<=day<=31):
        print("Invalid")
    else:
        print("Spring")
elif month == 'June':
    if not(1<=day<=30):
        print("Invalid")
    elif day<=20:
        print ("Spring")
    else:
        print("Summer")
elif month == 'July' or month == 'August':
    if not(1<=day<=31):
        print("Invalid")
    else: 
        print("Summer")
elif month == 'September':
    if not(1<=day<=30):
        print("Invalid")
    elif day<=21:
        print ("Summer")
    else:
        print ("Autumn")
elif month == "October":
    if not(1<=day<=31):
        print("Invalid")
    else:
        print("Autumn")
elif month == "November":
    if not(1<=day<=30):
        print("Invalid")
    else:
        print ("Autumn")
elif month == "December":
    if not(1<=day<=31):
        print("Invalid")
    elif day <=20:
        print ("Autumn")
    else:
        print ("Winter")
elif month == 'January':
    if not(1<=day<=31):
        print("Invalid")
    else:
        print("Winter")
elif month == "February":
    if not(1<=day<=29):
        print("Invalid")
else:
    print ("Winter")


"""
Write a program with total change amount as an integer input, and output the 
change using the fewest coins, one coin type per line. The coin types are Dollars, 
Quarters, Dimes, Nickels, and Pennies. 
Use singular and plural coin names as appropriate, like 1 Penny vs. 2 Pennies.
"""

total_change=int(input())

dollars=total_change//100
quarters=(total_change-dollars*100)//25
dimes=(total_change-dollars*100-quarters*25)//10
nickels=(total_change-dollars*100-quarters*25-dimes*10)//5
pennys=(total_change-dollars*100-quarters*25-dimes*10-nickels*5)//1

#no change 
if total_change<=0:
   print('No change')
#dollars
if 0<dollars<=1:
   print(dollars,'Dollar')
if dollars>1:
   print(dollars,'Dollars')
#quarters  
if 0<quarters<=1:
   print(quarters,'Quarter')
if quarters>1:
   print(quarters,'Quarters')
#dimes   
if 0<dimes<=1:
   print(dimes,'Dime')
if dimes>1:
   print(dimes,'Dimes')
#nickels   
if 0<nickels<=1:
   print(nickels,'Nickel')
if nickels>1:
   print(nickels,'Nickels')
#pennys
if 0<pennys<=1:
   print(pennys,'Penny')
if pennys>1:
   print(pennys,'Pennys')


"""
WHILE LOOP

A while loop is a construct that repeatedly executes an 
indented block of code (known as the loop body) as long as 
the loop's expression is True.


"""
g = 0
while g <= 2:
    print(g, end = ' ')
    g += 1
print()




