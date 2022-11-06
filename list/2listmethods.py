cars = ["mercedes", "lambo", "ferrari", "audi", "porche"]
cars.append("toyota")  # add element to end
print(cars)

cars.insert(0, "tesla")  # insert an element at a pos
print(cars)

# removes an element, not the index, but the element itself
cars.remove("audi")
print(cars)


numbers = [2, 5, 1, 6, 78, 2, 6]
print(max(numbers))
print(5 in numbers)  # check if an element is in list

# removes the last ele
print(cars.pop())

# gives the index of the first occurence of an item
print(cars.index("lambo"))

# count the occurence
print(numbers.count(3))

# sort a list
numbers.sort()  # .reverse() to sort in descenting
print(numbers)
