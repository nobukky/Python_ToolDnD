from data.data import Data
from item.character import Character, Race, Affinity, CharacterSchema
from item.item import Item, ItemSchema
from item.equipment import Equipment, EquipmentSchema
from platformdirs import user_cache_dir
import os
import json


def write_file(content: str, path: str):
    with open(path, 'w+') as file:
        file.write(content)

def read_file(path: str):
    if not os.path.exists(path):
        return ""

    tweets = []
    with open(path, 'r') as file:
        for line in file:
            tweets.append(json.loads(line))
    return tweets

def get_path():
    cache_directory = user_cache_dir("Dnd_asset_creator", "NBK")
    if not os.path.exists(cache_directory):
        os.makedirs(cache_directory)
    return cache_directory

def save_to_json(list, schema, file_name: str):
    items_json = ""
    for item in list:
        item_schema = schema()
        item_serialized = item_schema.dumps(item)
        items_json += json.dumps(item_serialized, sort_keys=True, indent=4)
    write_file(items_json, get_path() + file_name)

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


        cache_directory = get_path()

        characters_json = read_file(cache_directory + "\\characters.json")
        if characters_json != "":
            characters = CharacterSchema(many=True).load(characters_json)

        #items = ItemSchema().load(read_file(cache_directory + "\\items.json"))
        #equipments = EquipmentSchema().load(read_file(cache_directory + "\\equipments.json"))

        return Data(characters, items, equipments)

    @staticmethod
    def save_data_to_json(data):
        print("Saving data...")
        save_to_json(data.characters, CharacterSchema, "\\characters.json")
        save_to_json(data.items, ItemSchema,"\\items.json")
        save_to_json(data.equipments, EquipmentSchema,"\\equipments.json")
