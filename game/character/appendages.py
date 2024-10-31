from abc import ABC


class Appendage(ABC):
    def __init__(self, attribute: int = 0):
        if attribute < 0:
            raise ValueError("Attribute value cannot be negative")
        self.attribute = attribute

    def evolve(self, increment: int = 1) -> None:
        self.attribute += increment

    def modify_attacking_power(self, attacking_power: int) -> int:
        return 0


class CountBasedAppendage(Appendage):
    @property
    def count(self) -> int:
        return self.attribute

    @count.setter
    def count(self, value: int) -> None:
        self.attribute = value


class LevelBasedAppendage(Appendage):
    @property
    def level(self) -> int:
        return self.attribute

    @level.setter
    def level(self, value: int) -> None:
        self.attribute = value


class Legs(CountBasedAppendage):
    def can_hop(self) -> bool:
        return self.count >= 1

    def can_walk(self) -> bool:
        return self.count >= 2

    def can_run(self) -> bool:
        return self.count >= 2


class Wings(CountBasedAppendage):
    def can_fly(self) -> bool:
        return self.count >= 2


class Claws(LevelBasedAppendage):
    def modify_attacking_power(self, attacking_power: int) -> int:
        return attacking_power * (min(self.level + 1, 4))


class Teeth(LevelBasedAppendage):
    def modify_attacking_power(self, attacking_power: int) -> int:
        return attacking_power + (min(self.level * 3, 9))
