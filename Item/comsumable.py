from item import Item
from enums import Effect


class Armor(Item):

    def __init__(self, name: str, description: str, image, id: int,
                 power: int, effect: Effect):
        super.__init__().name = name
        super.__init__().description = description
        super.__init__().image = image
        super.__init__().id = id
        self.power = power
        self.effect = effect
