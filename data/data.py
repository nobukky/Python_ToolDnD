from item.character import Character
from item.item import Item
from item.equipment import Equipment


class Data:
    def __init__(self, characters: list[Character], items: list[Item], equipments: list[Equipment]):
        self.characters = characters
        self.items = items
        self.equipments = equipments