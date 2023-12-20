from enum import Enum
from misc.random import Random


class Race(Enum):
    HUMAN = 0,
    ORC = 1,
    ELF = 2



class Affinity(Enum):
    WARRIOR = 0
    MAGE = 1
    THIEF = 2


class Character:

    def __init__(self, name: str, background: str, image, id: int,
                 race: Race, affinity: Affinity, do_randomize_stats: bool):
        self.name = name
        self.background = background
        self.image = image
        self.id = id
        self.race = race
        self.affinity = affinity

        self.statistics: list[(str, int)] = list()
        self.set_statistics(do_randomize_stats)


    def set_statistics(self, do_randomize_stats):
        if do_randomize_stats:
            self.statistics.append(("Force", Random.roll_dice(1, 20)))
            self.statistics.append(("Dexterity", Random.roll_dice(1, 20)))
            self.statistics.append(("Intelligence", Random.roll_dice(1, 20)))
            self.statistics.append(("Luck", Random.roll_dice(1, 20)))
            self.statistics.append(("Health Points", Random.roll_dice(1, 20)))
        else:
            self.statistics.append(("Force", Random.roll_dice(3, 6)))
            self.statistics.append(("Dexterity", Random.roll_dice(3, 6)))
            self.statistics.append(("Intelligence", Random.roll_dice(3, 6)))
            self.statistics.append(("Luck", Random.roll_dice(3, 6)))
            self.statistics.append(("Health Points", Random.roll_dice(3, 6)))