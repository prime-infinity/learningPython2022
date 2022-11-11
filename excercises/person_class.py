class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f'{self.name} greets you ')


john = Person("john")
john.greet()
