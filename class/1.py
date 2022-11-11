''' to clarify or simplify,classes are used to model
more complex data types and create our own methods to it.
similar to how we create structs which are containers used to model
more complex data types in golang
'''


class Point:
    # methods, which are just func in a class
    def move(self):
        print("is moving")

    def draw(self):
        print("is drawing")


''' 
    the concept of oop and classes are really amazing
    a class is simply the blueprint of a custom data type,
    to which we can create multiple instances of
'''

# create a new instance of Point class

point1 = Point()
point1.draw()
# we can also set attributes to the instance
point1.x = 10
point1.y = 20
print(point1.x)
