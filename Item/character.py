from item import Item
from enums import Race, Affinity


class Character(Item):

    def __init__(self, name: str, description: str, image, id: int,
                 race: Race, affinity: Affinity, do_randomize_stats: bool, statistics: (str, int)):
        super.__init__().name = name
        super.__init__().description = description
        super.__init__().image = image
        super.__init__().id = id
        self.race = race
        self.affinity = affinity
        self.do_randomize_stats = do_randomize_stats
        self.statistics = statistics
