from enum import Enum


class Effect(Enum):
    NONE = 0
    FIRE = 1
    POISON = 2


class Range(Enum):
    CLOSE = 0
    DISTANT = 1


class Equipment:
    def __init__(self, name: str, description: str, image, id: int):
        self.name = name
        self.description = description
        self.image = image
        self.id = id


class Weapon(Equipment):

    def __init__(self, name: str, description: str, image, id: int,
                 effect: Effect, range: Range):
        super.__init__().name = name
        super.__init__().description = description
        super.__init__().image = image
        super.__init__().id = id
        self.effect = effect
        self.range = range


class Shield(Equipment):

    def __init__(self, name: str, description: str, image, id: int,
                 defence: int):
        super.__init__().name = name
        super.__init__().description = description
        super.__init__().image = image
        super.__init__().id = id
        self.defence = defence


class Armor(Equipment):

    def __init__(self, name: str, description: str, image, id: int,
                 resistance: Effect):
        super.__init__().name = name
        super.__init__().description = description
        super.__init__().image = image
        super.__init__().id = id
        self.resistance = resistance

