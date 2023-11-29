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


