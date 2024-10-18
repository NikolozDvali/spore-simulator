from sporesimulator.game.character.appendages import Legs, Wings, Claws, Teeth
from sporesimulator.game.core.constants import DEFAULT_HEALTH, DEFAULT_STAMINA, DEFAULT_ATTACK_POWER


class PositionManager:
    def __init__(self, position: int = 0):
        self.position = position

class AppendageManager:
    def __init__(self,
                 legs: Legs | None = None,
                 wings: Wings | None = None,
                 claws: Claws | None = None,
                 teeth: Teeth | None = None):
        self.legs = legs if legs is not None else Legs()
        self.wings = wings if wings is not None else Wings()
        self.claws = claws if claws is not None else Claws()
        self.teeth = teeth if teeth is not None else Teeth()

    """Common attribute getters"""

    @property
    def wing_count(self):
        return self.wings.count()

    @property
    def leg_count(self):
        return self.legs.count()

    @property
    def teeth_level(self):
        return self.teeth.level

    @property
    def claw_level(self):
        return self.claws.level

    """Common attribute setters"""

    @leg_count.setter
    def leg_count(self, count: int):
        self.legs.count = count

    @wing_count.setter
    def wing_count(self, count: int):
        self.wings.count = count

    @teeth_level.setter
    def teeth_level(self, level: int):
        self.teeth.level = level

    @claw_level.setter
    def claw_level(self, level: int):
        self.claws.level = level

    """Common methods"""

    def calculate_attack_power(self, base_attack_power: int) -> int:
        attack_power = base_attack_power
        if self.claws:
            attack_power = self.claws.modify_attacking_power(attack_power)
        if self.teeth:
            attack_power = self.teeth.modify_attacking_power(attack_power)
        return attack_power

class CharacterStatsManager:
    def __init__(self,
                 health: int = DEFAULT_HEALTH,
                 stamina: int = DEFAULT_STAMINA,
                 attacking_power: int = DEFAULT_ATTACK_POWER) -> None:
        self.health = health
        self.stamina = stamina
        self.attacking_power = attacking_power
