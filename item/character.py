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


class Character:
    def __init__(self, name: str, description: str, image_path: str, id: int, race: Race, affinity: Affinity, statistics: list[int]):
        self.name: str = name
        self.description: str = description
        self.image_path: str = image_path
        self.id: int = id

        self.race: Race = race
        self.affinity: Affinity = affinity
        self.statistics: list[int] = statistics


class CharacterSchema(Schema):
    name = fields.Str()
    description = fields.Str()
    image_path = fields.Str()
    id = fields.Int()

    race = EnumField(Race)
    affinity = EnumField(Affinity)
    statistics = fields.List(fields.Int())