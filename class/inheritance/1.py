# share or inherit similar behaviors

class Mammal:
    def walk(self):
        print("is walking")


# will inherit all methods of mammal class,thus becoming its child
class Dog(Mammal):
    def bark(self):
        print("dog is barking")


class Cat(Mammal):
    pass  # tell the interpreter to fuck off


german_shephard = Dog()
german_shephard.walk()  # inherited method
german_shephard.bark()
