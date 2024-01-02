from data.data import Data
from item.character import Character, Race, Affinity, CharacterSchema
from platformdirs import user_cache_dir
from item.item import Item
from item.equipment import Equipment
import os
import json


def write_file(content: str, path: str):
    with open(path, 'w+') as file:
        file.write(content)

class Serializer:

    @staticmethod
    def load_data_from_json():
        print("Loading data...")

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

    @staticmethod
    def save_data_to_json(data):
        print("Saving data...")

        # getting data cache directory
        cache_directory = user_cache_dir("Dnd_asset_creator", "NBK")
        if not os.path.exists(cache_directory):
            os.makedirs(cache_directory)

        # serialize and store characters data
        characters_json = ""
        for character in data.characters:
            characters_schema = CharacterSchema()
            characters_serialized = characters_schema.dump(character)
            characters_json += json.dumps(characters_serialized, indent=4)
        write_file(characters_json, cache_directory + "\\characters.json")
