from enum import Enum
from marshmallow import Schema, fields
from marshmallow_enum import EnumField


class Effect(Enum):
    NONE = 0
    FIRE = 1
    POISON = 2
    HEAL = 3


class Item:
    def __init__(self, name, description, image, id, effect: Effect = Effect.NONE, strength: int = None):
        self.name = name
        self.description = description
        self.image = image
        self.id = id

        self.effect = effect
        self.strength = strength


class ItemSchema(Schema):
    name = fields.Str()
    description = fields.Str()
    image = fields.Str()
    id = fields.Int()

    strength = fields.Int()
    effect = EnumField(Effect)
