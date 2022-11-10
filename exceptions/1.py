try:
    age = int(input("age:"))
    print(age)
except ValueError:  # the kind of expected err,may also be left empt
    print("invalid value")
except:
    print("something went wrong")
finally:  # will always run
    print("done")
