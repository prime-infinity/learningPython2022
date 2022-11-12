# find the max number of a list
numbers = [2, 5, 1, 7, 8, 9, 22, 63, 38, 84, 12, ]
# be careful not to overide python's built in function
# with your own
max_number = numbers[0]
for n in numbers:
    if n > max_number:
        max_number = n

print(max_number)

# or just use the max() function
print(max(numbers))
