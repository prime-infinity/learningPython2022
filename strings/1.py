# string operations
course = "python for beginners"
# strings in python are objects with lots of methods
# associated with them

print(course.upper())
# uppercase of the string
# note that the methods do not mutate the orignal
# string, but return a new mutated string

# there are lots of string operations
course.lower()
course.find("b")
# attempts to find the string in the arguement and return its index pos
print(course.replace("python", "golang"))
# find and replace a string or series of string

print("python" in course)
# check if a string is in another string, returns true or false instead of index pos
