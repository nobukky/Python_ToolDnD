from enum import Enum


class Race(Enum):
    HUMAN = 0,
    ORC = 1,
    ELF = 2


class Affinity(Enum):
    WARRIOR = 0
    MAGE = 1
    THIEF = 2


class Effect(Enum):
    NONE = 0
    FIRE = 1
    POISON = 2
    HEAL = 3


class Range(Enum):
    CLOSE = 0
    DISTANT = 1
