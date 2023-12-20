from item import Item
from enums import Effect, Range


class Weapon(Item):

    def __init__(self, name: str, description: str, image, id: int,
                 effect: Effect, range: Range):
        super.__init__().name = name
        super.__init__().description = description
        super.__init__().image = image
        super.__init__().id = id
        self.effect = effect
        self.range = range
