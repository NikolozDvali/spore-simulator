from sporesimulator.game.character.appendages import Legs, Wings, Claws, Teeth
from sporesimulator.game.core.constants import DEFAULT_HEALTH, DEFAULT_STAMINA, DEFAULT_ATTACK_POWER
from sporesimulator.game.move.move import Move


class PositionManager:
    def __init__(self, position: int = 0):
        self.position = position

    def can_move_to(self, position: int) -> bool:
        return position >= 0

    def move(self, new_position: int) -> None:
        if new_position < 0:
            raise ValueError("Can't move to negative position!")
        self.position = new_position

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

    @property
    def wing_count(self):
        return self.wings.count()

    @wing_count.setter
    def wing_count(self, count: int):
        self.wings.count = count

    @property
    def leg_count(self):
        return self.legs.count()

    @leg_count.setter
    def leg_count(self, count: int):
        self.legs.count = count

    @property
    def teeth_level(self):
        return self.teeth.level

    @teeth_level.setter
    def teeth_level(self, level: int):
        self.teeth.level = level

    @property
    def claw_level(self):
        return self.claws.level

    @claw_level.setter
    def claw_level(self, level: int):
        self.claws.level = level

    """Movement check"""

    def supports_movement(self, move_protocol: type[Move]):
        move_type = move_protocol.__name__.lower()
        move_methods = {
            'crawl': lambda: True,
            'hop': self.legs.can_hop,
            'walk': self.legs.can_walk,
            'run': self.legs.can_run,
            'fly': self.wings.can_fly,
        }

        return move_methods.get(move_type, lambda: False)()

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

    def can_use_stamina(self, required_stamina: int) -> bool:
        return self.stamina >= required_stamina

    def use_stamina(self, stamina_cost: int = 0, required_stamina: int = 0) -> None:
        if self.stamina < required_stamina:
            raise ValueError("Not enough stamina!")
        self.stamina -= stamina_cost
