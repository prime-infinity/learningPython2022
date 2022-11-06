command = ""
started = ""

while command != "quit":  # the mans imple uses while True, to run until broken
    command = input("> ").lower()
    if command == "help":
        print(''' 
start - start the car
stop - stop the car
quit - end the game
                  ''')
    elif command == "start":
        if started:
            print("car already started")
        else:
            started = True
            print("car started")
    elif command == "stop":
        if started == False:
            print("car already stopped")
        else:
            print("car stopped")
            started = False
    elif command == "quit":
        print("game ended")
        break
    else:
        print("i dont understand your command")
