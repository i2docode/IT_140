#!/usr/bin/python3
"""
in-place modification - list mutability; growing and shrinking.
lists are mutable and is thus able to grow and shrink without the program having to replace the entire list with an updated copy.

del list[i] - will delete the element at the specified list index.

"""
test_list = [0, 1, 2]

# list element reassignment.
# deleting a list item.
del test_list[len(test_list) - 1]
print(test_list)

# list methods - can perform a useful operation on a list such as adding or removing elements, sorting, reversing, etc.
# list.append(x) - Add an item to the end of list.
test_list.append(2)
print(test_list)

# # adding list elements
# list.extend([x]) - Add all items in [x] to list.

# list.insert(i, x)	- Insert x into list before position i.


# # removing list elements
# list.remove(x) - Remove first item from list with value x.

# list.pop() - Remove and return last item in list.

# list.pop(i) - Remove and return item at position i in list.



# # modifying lists
# list.sort() - Sort the items of list in-place.

# list.reverse() - Reverse the elements of list in-place.


# # miscellaneous list methods

# list.index(x)	- Return index of first item in list with value x.

# list.count(x)	- Count the number of times value x is in list.

# list comprehensions

"""
A list comprehension has three components:

An expression component to evaluate for each element in the iterable object.
A loop variable component to bind to the current iteration element.
An iterable object component to iterate over (list, string, tuple, enumerate, etc).

list comprehension - iterates over a list, modifies each element, 
and returns a new list consisting of the modified elements.


"""
# using list comprehension to add 10 to each element in a list.
negatives_list = [-5, -4, -3]

add_ten_to_negatives = [ (i+10) for i in negatives_list ]
print(add_ten_to_negatives)

# using list comprehension to convert to each element into float data types.
ints_list = [5, 10, 200]

floats_list = [float(i) for i in ints_list]
print(floats_list)

# using list comprehension to convert user input integers into integers.
num_input = '4 6 100'

convert_list = [int(i) for i in num_input.split()]
print(convert_list)

# using list comprehension to find the sum of each row in 2d list.
two_dimesional_list = [[5, 10], [1]]

sum_list = [sum(row) for row in two_dimesional_list]
print(sum_list)

"""
write a list comprehension that contains elements 
with the desired values. Use the name 'i' as the loop variable.
"""
x = [2, 4, 6]
x = [i * 2 for i in x]
print(x)

"""
Conditional list comprehensions
"""
# conditional list comprehension printing all even numbers.
ints_list = [5, 4, 3]

even_ints = [i for i in ints_list if i % 2 == 0]
print(even_ints)

# conditional list comprehension printing all numbers less than 5.
less_than_five = [i for i in ints_list if i < 5]
print(less_than_five)

# conditional list comprehension that adds 10 to each number less than 5.
add_ten_to_smaller_than_5 = [i + 10 for i in ints_list if i < 5]
print(add_ten_to_smaller_than_5)

# conditional list comprehension that adds negative 10 to 5.
add_neg_ten_to_five = [i + -10 for i in ints_list if i == 5]
print(add_neg_ten_to_five)

# dictionary objects
dict0 = {
    '1':'a',
    '2':'b',
    '3':'c'
}
# dict.cleat() - removes all items from the dictionary,


# dict.get(key, default) - reads key:value from dictionary.
print(dict0.get('1', 'N/A'))


# dictA.update(dictB) - merges first dictionary with a second.
    # first dictionary key-values are overwritten


# dict.pop() - removes and returns key-value from the dictionary.
    # default returned if key-value does not returned.


dict0_pop = dict0.pop('3')
print(dict0_pop)
print(dict0)
print()

_dict = dict(bananas=1.59, fries=2.39, burger=3.50, sandwich=2.99)
_dict.update(dict(soda=1.49, burger=3.69))
burger_price = _dict.get('burger', 0)
print(burger_price)



_dict['burger'] = _dict['sandwich']
val = _dict.pop('sandwich')
print(_dict['burger'])

"""
iterating over a dictionary
retrieve or modify dictionary elements.

access dictionaty elements
.items()
.keys()
.values()
"""
for key in dict0:
    print(key)

print()

for key, val in dict0.items():
    print(key, val)


