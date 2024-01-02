from data.data import Data
from item.character import Character, Race, Affinity
from item.item import Item
from item.equipment import Equipment


class Serializer:

    @staticmethod
    def save_data_to_json(data):
        # serialize data lists to json
        # save json data
        pass

    @staticmethod
    def load_data_from_json():
        # load data lists from json

        # debug data
        bob = Character("Bob", "Child of the moon", "image", 0, Race.HUMAN, Affinity.MAGE, True)
        oli = Character("Oli", "Destructor of worlds", "image", 1, Race.ORC, Affinity.WARRIOR, True)
        characters = [bob, oli]

        axe = Equipment("Axe", "Heavy black axe", "image", 0)
        pickaxe = Equipment("Pickaxe", "heavy pickaxe", "image", 1)
        equipments = [axe, pickaxe]

        potion = Item("Potion", "Heals 2 health points", "image", 0)
        items = [potion]

        return Data(characters, items, equipments)
