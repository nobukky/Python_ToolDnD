from random import randint


class Dice:

    @staticmethod
    def roll_dice(amount, value):
        """
        Returns the sum of 'amount' random numbers between 1 and 'value'
        """
        output = 0
        for i in range(amount):
            output += randint(1, value)
        return output