from enum import Enum
from marshmallow import Schema, fields
from marshmallow_enum import EnumField


class Effect(Enum):
    NONE = 0
    FIRE = 1
    POISON = 2
    ELECTRICITY = 3


class Range(Enum):
    CLOSE = 0
    DISTANT = 1
    HYBRID = 2
    THROWABLE = 3


class EquipmentType(Enum):
    WEAPON = 0
    SHIELD = 1
    ARMOR = 2
    TOOL = 3


class Equipment:
    def __init__(self, name: str, description: str, image, id: int, type: EquipmentType = None, effect: Effect = Effect.NONE, range: Range = None, strength: int = None, defense: int = None):
        self.name = name
        self.description = description
        self.image = image
        self.id = id

        self.type = type
        self.effect = effect
        self.range = range
        self.strength = strength
        self.defense = defense


class EquipmentSchema(Schema):
    name = fields.Str()
    description = fields.Str()
    image = fields.Str()
    id = fields.Int()

    type = EnumField(EquipmentType)
    effect = EnumField(Effect)
    range = EnumField(Range)
    strength = fields.Int()
    defense = fields.Int()