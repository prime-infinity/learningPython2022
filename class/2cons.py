# using constructors
''' a constructor is a function that gets
    called at the time of creating an instance of an object
'''


class Point:

    # constructor method gets called at class init
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # methods, which are just func in a class
    def move(self):
        print("is moving")

    def draw(self):
        print("is drawing")


point1 = Point(10, 20)
point1.x = 12  # we can also mutate the values
print(point1.y)
