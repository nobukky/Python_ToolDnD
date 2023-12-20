from enum import Enum

class Effect(Enum):
    NONE = 0
    FIRE = 1
    POISON = 2
    HEAL = 3


class Item:

    def __init__(self, name, description, image, id):
        self.name = name
        self.description = description
        self.image = image
        self.id = id


class Consumable(Item):

    def __init__(self, name: str, description: str, image, id: int,
                 power: int, effect: Effect):
        super.__init__().name = name
        super.__init__().description = description
        super.__init__().image = image
        super.__init__().id = id
        self.power = power
        self.effect = effect
