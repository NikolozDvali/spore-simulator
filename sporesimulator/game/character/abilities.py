from typing import Protocol

from sporesimulator.game.character.character import Character


class Move(Protocol):
    def required_stamina(self) -> int:
        pass

    def stamina_cost(self) -> int:
        pass

    def speed(self) -> int:
        pass

    def can_do(self, character: Character) -> bool:
        pass

class Crawl(Move):
    def required_stamina(self) -> int:
        return 0

    def stamina_cost(self) -> int:
        return 1

    def speed(self) -> int:
        return 1

    def can_do(self, character: Character) -> bool:
        return character.stats_manager.stamina >= self.required_stamina()

class Hop(Move):
    def required_stamina(self) -> int:
        return 20

    def stamina_cost(self) -> int:
        return 2

    def speed(self) -> int:
        return 3

    def can_do(self, character: Character) -> bool:
        return character.appendage_manager.legs.count > 1 and character.stats_manager.stamina >= self.required_stamina()

class Walk(Move):
    def required_stamina(self) -> int:
        return 40

    def stamina_cost(self) -> int:
        return 2

    def speed(self) -> int:
        return 4

    def can_do(self, character: Character) -> bool:
        return character.appendage_manager.legs.count > 2 and character.stats_manager.stamina >= self.required_stamina()

class Run(Move):
    def required_stamina(self) -> int:
        return 60

    def stamina_cost(self) -> int:
        return 4

    def speed(self) -> int:
        return 6

    def can_do(self, character: Character) -> bool:
        return character.appendage_manager.legs.count > 2 and character.stats_manager.stamina >= self.required_stamina()


class Fly(Move):
    def required_stamina(self) -> int:
        return 80

    def stamina_cost(self) -> int:
        return 4

    def speed(self) -> int:
        return 8

    def can_do(self, character: Character) -> bool:
        return character.appendage_manager.wings.count > 2 and character.stats_manager.stamina >= self.required_stamina()
