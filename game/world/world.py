from typing import Dict

from game.core.common import Entity, Coordinate

class World:
    def __init__(self):
        self.entities: Dict[Entity, Coordinate] = {}