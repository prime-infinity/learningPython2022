numbers = [1, 2, 3, 4, 5, 6, 7]
count = 0
for i in numbers:
    count = count + i
    print(i)

print(count)

# using a while loop, not recommended

i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1
