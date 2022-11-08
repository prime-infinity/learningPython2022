'''numbers = [2, 3, 1, 4, 2, 2, 4, 6, 3, 6, 3, 2, 6, 3]

index = 0
length = len(numbers)

while index < length:
    saved = numbers[index]

    if numbers.count(saved) > 1:
        print("more that once")
        numbers.pop(index)
    elif numbers.count(saved) == 1:
        print("just once")

    index = index + 1

print(numbers)'''

# the above method failed misrbly

numbers = [2, 3, 2, 3, 1, 2, 4, 6, 4, 6, 7, 8, 4, 5, 6, 8]
uniques_one = []

for n in numbers:
    if numbers.count(n) == 1:
        uniques_one.append(n)

# this version of unique list is truly unique, it removes
# both copy and original values
print(uniques_one)

uniques_two = []

for n in numbers:
    if not n in uniques_two:
        uniques_two.append(n)

# this version of uniq removes only copies
print(uniques_two)
