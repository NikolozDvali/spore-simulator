from typing import Protocol


class Characteristic(Protocol):
    def evolve(self):
        pass

class Limbs(Characteristic):
    def __init__(self, count: int = 0):
        if count < 0:
            raise ValueError("Limb count cannot be negative")
        self.count = count

    def evolve(self, number_of_additional_limbs: int = 1):
        self.count += number_of_additional_limbs

class Legs(Limbs):
    def can_hop(self):
        return self.count >= 1

    def can_walk(self):
        return self.count >= 2

    def can_run(self):
        return self.count >= 2

class Wings(Limbs):
    def can_fly(self):
        return self.count >= 2

class Appendage(Characteristic):
    def __init__(self, level: int = 0):
        if level < 0:
            raise ValueError("Appendage level cannot be negative")
        self.level = level

    def evolve(self, level_increment: int = 1):
        self.level += level_increment

class Claws(Appendage):
    def attacking_power_multiplier(self):
        if self.level == 0:
            return 1
        elif self.level == 1:
            return 2
        elif self.level == 2:
            return 3
        elif self.level >= 3:
            return 4

class Teeth(Appendage):
    def attacking_power_additional(self):
        if self.level == 0:
            return 0
        elif self.level == 1:
            return 3
        elif self.level == 2:
            return 6
        elif self.level >= 3:
            return 9