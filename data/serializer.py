from data.data import Data
from item.character import Character, Race, Affinity, CharacterSchema
from item.item import Item, ItemSchema
from item.equipment import Equipment, EquipmentSchema, EquipmentType, Effect, Range
from platformdirs import user_cache_dir
from misc.image import Image
import os
import json


class Serializer:

    @staticmethod
    def load_data_from_json():
        """
        Return a newly created data from debug line. (The deserialization system doesn't work)
        """

        # character
        luffy = Character("Luffy", "Drums of Freedom", Image.LUFFY, 483347, Race.GOD, Affinity.WARRIOR, [20, 16, 4, 13, 15])
        robert_oppenheimer = Character("Robert", "Destroyer of Worlds", Image.ROBERT_OPPENHEIMER, 839650, Race.HUMAN, Affinity.ENGINEER, [7, 9, 20, 10, 11])
        characters = [luffy, robert_oppenheimer]

        # equipments
        axe = Equipment("Axe", "Heavy black axe", "empty", 592304, EquipmentType.WEAPON, Effect.NONE, Range.THROWABLE, 9, 3)
        hylian_shield = Equipment("Hylian Shield", "\"Link, yamete!\", Zelda", "empty", 345298, EquipmentType.SHIELD, Effect.ELECTRICITY, Range.CLOSE, 3, 8)
        equipments = [axe, hylian_shield]

        # items
        healing_potion = Item("Heal Potion", "Heals 2 health points", "empty", 923805, Effect.NONE, 2)
        fire_vial = Item("Fire vial", "Deals 4 damages immediately", "empty", 199823, Effect.FIRE, 4)
        poison_vial = Item("Poison vial", "Deals 5 damages over time", "empty", 892375, Effect.POISON, 5)
        items = [healing_potion, fire_vial, poison_vial]

        ### uncompleted attempts to deserialize the json data
        #cache_directory = get_path()
        #characters_json = read_file(cache_directory + "\\characters.json")
        #if characters_json != "":
        #    characters = CharacterSchema(many=True).load(characters_json)
        #items = ItemSchema().load(read_file(cache_directory + "\\items.json"))
        #equipments = EquipmentSchema().load(read_file(cache_directory + "\\equipments.json"))

        print("SERIALIZER: debug data loaded")
        return Data(characters, items, equipments)

    @staticmethod
    def save_data_to_json(data):
        """
        Save the three list of the given data into a json file
        """
        Serializer._save_to_json(data.characters, CharacterSchema, "\\characters.json")
        Serializer._save_to_json(data.items, ItemSchema,"\\items.json")
        Serializer._save_to_json(data.equipments, EquipmentSchema,"\\equipments.json")
        print("SERIALIZER: data saved to json (c.g.: appdata/Local/NBK/Dnd_asset_creator/Cache)")


    @staticmethod
    def _write_file(content: str, path: str):
        """
        Write down all the given content into a json file at the given path
        """
        with open(path, 'w+') as file:
            file.write(content)

    @staticmethod
    def _read_file(path: str):
        """
        Return a list of lines from the json file at the given path
        """
        # null exception
        if not os.path.exists(path):
            return ""

        # loads the json line by line
        tweets = []
        with open(path, 'r') as file:
            for line in file:
                tweets.append(json.loads(line))
        return tweets

    @staticmethod
    def _get_path():
        """
        Return the path of the data appdata cache directory
        """
        cache_directory = user_cache_dir("Dnd_asset_creator", "NBK")
        if not os.path.exists(cache_directory):
            os.makedirs(cache_directory)
        return cache_directory

    @staticmethod
    def _save_to_json(list, schema, file_name: str):
        """
        Serialize the given list with in the given schema
        Then, save to serialized list to json
        """
        items_json = ""
        for item in list:
            # serialize data to json
            item_schema = schema()
            item_serialized = item_schema.dump(item)
            # gather all the json
            items_json += json.dumps(item_serialized, sort_keys=True, indent=4)
        Serializer._write_file(items_json, Serializer._get_path() + file_name)