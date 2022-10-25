birth_year = input("enter your birth year ")
#age = 2022 - birth_year
# the above line will cause an error because
# we are trying to subtract from a string, the value received
# from the "input()" is a string, hence we need to convert it to int


age = 2022 - int(birth_year)
# the above code "int()" converts to an int
print(age)

# other type conversions
float()  # convert value to float
str()  # convert value to string
bool()  # convert value to bool
