from random import randint


class Random:

    def __init__(self):
        pass


    @staticmethod
    def roll_dice(amount, value):
        sum = 0
        for i in range(amount):
            sum += randint(1, value)
        return sum