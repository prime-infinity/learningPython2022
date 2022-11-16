# share or inherit similar behaviors
''' 
in this example, only methods are inherited from
the super class, but attributes can also be inherited
as shown in 2.py 
'''


class Mammal:
    def walk(self, breed):
        print(f'{breed} is walking')


# will inherit all methods of mammal class,thus becoming its child
class Dog(Mammal):
    def __init__(self, breed):
        self.breed = breed

    def bark(self):
        print("dog is barking")


class Cat(Mammal):
    pass  # tell the interpreter to fuck off


german_shephard = Dog("german_sephard")
german_shephard.walk(german_shephard.breed)  # inherited method
# german_shephard.bark()
# print()
