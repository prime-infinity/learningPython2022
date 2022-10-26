weight = float(input("enter your weight "))
unit = input("(K)g or (L)bs: ")
if unit == "L" or unit == "l":
    print("your weight in kg is:", weight*0.453, weight)
elif unit == "k" or unit == "K":
    print("your weight in lbs is:", weight*2.20, weight)
