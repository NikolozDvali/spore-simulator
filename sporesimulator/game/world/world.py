from typing import Dict

from sporesimulator.game.character.character import Character
from sporesimulator.game.core.common import Coordinate


class World:
    def __init__(self):
        self.characters: Dict[Character, Coordinate] = {}

    def add_character(self, character: Character, coordinate: Coordinate):
        self.characters[character] = coordinate
        