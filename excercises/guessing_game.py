number = 8
tries = 3
attempt = 0

while attempt < tries:
    user_input = int(input("guess "))
    attempt += 1
    if user_input == number:
        print("correct")
        break
else:
    # code written here will work if the while loop completes
    # without an immediate break
    print("too much attempts")
