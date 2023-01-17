listt = [1, 2, 3, 4, 5, 6, 7, 8]

confirm_list = [i >= 2 for i in listt]
print(confirm_list)

# you should understand this syntax

# you can create a new list by applying an expression
# to each existing item of an already exsisting list

numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(squares)
# in the above, the new list will be the squares
# of all the items in the numbers list

'''
It's also possible to include conditionals in list
comprehensions by adding an if statement after the
for loop. This will filter the items in the iterable
based on the condition, only including items that
meet the condition in the new list.
'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = [x**2 for x in numbers if x % 2 == 0]
print(even_squares)

# this is a really nice feature
