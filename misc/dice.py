from random import randint


class Dice:

    def __init__(self):
        pass


    @staticmethod
    def roll_dice(amount, value):
        output = 0
        for i in range(amount):
            output += randint(1, value)
        return output