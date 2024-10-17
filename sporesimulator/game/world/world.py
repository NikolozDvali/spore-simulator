from typing import Dict

from sporesimulator.game.character.character import Character


class World:
    def __init__(self):
        self.characters: Dict[Character, int] = {}

    def add_character(self, character: Character, coordinate: int):
        self.characters[character] = coordinate
