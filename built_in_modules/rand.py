import random


for i in range(3):
    print(random.random())  # print random between 0 and 1
    print(random.randint(10, 20))  # random between two ints

members = ["john", "peter", "james", "judas"]
print(random.choice(members))  # randomly pick from list
