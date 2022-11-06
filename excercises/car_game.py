command = "s"

while command != "quit":
    command = input("> ").lower()
    if command == "help":
        print(''' start - start the car
                  stop - stop the car
                  quit - end the game
                  ''')
    elif command == "start":
        print("car started")
    elif command == "stop":
        print("car stopped")
    elif command == "quit":
        print("game ended")
        break
    else:
        print("i dont understand your command")
