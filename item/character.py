from enum import Enum
from misc.dice import Dice
from marshmallow import Schema, fields
from marshmallow_enum import EnumField


class Race(Enum):
    HUMAN = 0,
    ORC = 1,
    ELF = 2



class Affinity(Enum):
    WARRIOR = 0
    MAGE = 1
    THIEF = 2


def get_statistics(do_randomize_stats):
    statistics: list[Stat] = list()
    if do_randomize_stats:
        statistics.append(Stat("Force", Dice.roll_dice(1, 20)))
        statistics.append(Stat("Dexterity", Dice.roll_dice(1, 20)))
        statistics.append(Stat("Intelligence", Dice.roll_dice(1, 20)))
        statistics.append(Stat("Luck", Dice.roll_dice(1, 20)))
        statistics.append(Stat("Health Points", Dice.roll_dice(1, 20)))
    else:
        statistics.append(Stat("Force", Dice.roll_dice(3, 6)))
        statistics.append(Stat("Dexterity", Dice.roll_dice(3, 6)))
        statistics.append(Stat("Intelligence", Dice.roll_dice(3, 6)))
        statistics.append(Stat("Luck", Dice.roll_dice(3, 6)))
        statistics.append(Stat("Health Points", Dice.roll_dice(3, 6)))
    return statistics


class Stat:
    def __init__(self, name: str, value: int):
        self.name: str = name
        self.value: int = value


class StatSchema(Schema):
    name = fields.Str()
    value = fields.Int()


class Character:
    def __init__(self, name: str, description: str, image_path: str, id: int, race: Race, affinity: Affinity, do_randomize_stats: bool):
        self.name: str = name
        self.description: str = description
        self.image_path: str = image_path
        self.id: int = id

        self.race: Race = race
        self.affinity: Affinity = affinity
        self.statistics: list[Stat] = get_statistics(do_randomize_stats)


class CharacterSchema(Schema):
    name = fields.Str()
    description = fields.Str()
    image_path = fields.Str()
    id = fields.Int()
    race: EnumField(Race)
    affinity: EnumField(Affinity)
    statistics = fields.List(fields.Nested(StatSchema))