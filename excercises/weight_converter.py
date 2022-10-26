weight = float(input("enter your weight "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "L":
    print("your weight in kg is:", weight*0.453)
elif unit.upper() == "K":
    print("your weight in lbs is:", weight/0.45)
