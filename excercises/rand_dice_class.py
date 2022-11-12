import random


class Dice:
    '''
    this is not needed, except to add
    more customization
    def __init__(self, x, y):
        self.x = x
        self.y = y
    '''

    def roll(self):
        return (random.randint(1, 6), random.randint(1, 6))


dice_one = Dice()
print(dice_one.roll())
