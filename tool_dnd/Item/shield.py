from item import Item


class Shield(Item):

    def __init__(self, name: str, description: str, image, id: int,
                 defence: int):
        super.__init__().name = name
        super.__init__().description = description
        super.__init__().image = image
        super.__init__().id = id
        self.defence = defence
