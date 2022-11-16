'''
in this example, attributes of the super
or the parent class are also inherited
'''


class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self, attri):
        print(f'is {attri}')

    def show(self):
        print(f'my name is {self.name} and i am {self.age} old')


class Dog(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)  # call a method from the super class
        self.color = color

    ''' 
    what the above does,is so that we dont need to replicate code
    to init our dog class, from attributes already in the super class
    '''

    def show(self):
        print(f'i am {self.name} and my color is {self.color}')


class Cat(Pet):
    pass


p = Pet("tim", 19)
p.show()

c = Cat("bil", 4)
c.show()
'''
as you can see, the "Cat" class inherits
both attributes and methods from its
parent "Pet" class
'''
c.speak("meowing")

d = Dog("jimm", 12, "red")
d.show()
