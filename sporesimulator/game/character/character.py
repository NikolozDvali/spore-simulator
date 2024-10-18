from enum import Enum
from typing import Self, List

from sporesimulator.game.character.appendages import Legs, Wings, Claws, Teeth
from sporesimulator.game.core.constants import DEFAULT_HEALTH, DEFAULT_ATTACK_POWER, DEFAULT_STAMINA, DEFAULT_POSITION


class Direction(Enum):
    RIGHT = 1
    LEFT = -1

class Move:
    def __eq__(self, other):
        return isinstance(other, Move)

    def speed(self) -> int:
        return 0

    def can_do(self, character: 'Character') -> bool:
        return False

    def uses_stamina(self) -> int:
        return 0

# noinspection PyMethodMayBeStatic
class Crawl(Move):
    def requires_stamina(self):
        return 1

    def can_do(self, character: 'Character'):
        return character.stats_manager.stamina > self.requires_stamina()

    def speed(self):
        return 1

    def uses_stamina(self):
        return 1

# noinspection PyMethodMayBeStatic
class Hop(Move):
    def requires_stamina(self):
        return 21

    def can_do(self, character: 'Character'):
        return character.stats_manager.stamina > self.requires_stamina() and character.appendage_manager.legs.can_hop()

    def speed(self):
        return 3

    def uses_stamina(self):
        return 2

# noinspection PyMethodMayBeStatic
class Walk(Move):
    def requires_stamina(self):
        return 41

    def can_do(self, character: 'Character'):
        return character.stats_manager.stamina > self.requires_stamina() and character.appendage_manager.legs.can_walk()

    def speed(self):
        return 4

    def uses_stamina(self):
        return 2

# noinspection PyMethodMayBeStatic
class Run(Move):
    def requires_stamina(self):
        return 61

    def can_do(self, character: 'Character'):
        return character.stats_manager.stamina > self.requires_stamina() and character.appendage_manager.legs.can_run()

    def speed(self):
        return 6

    def uses_stamina(self):
        return 4

# noinspection PyMethodMayBeStatic
class Fly(Move):
    def requires_stamina(self):
        return 81

    def can_do(self, character: 'Character'):
        return character.stats_manager.stamina > self.requires_stamina() and character.appendage_manager.wings.can_fly()

    def speed(self):
        return 8

    def uses_stamina(self):
        return 4

class PositionManager:
    def __init__(self, position: int = 0):
        # TODO: check position >= 0
        self.position = position

    def move(self, move: Move, direction: Direction):
        new_position = self.position
        if direction == Direction.RIGHT:
            new_position += move.speed()
        elif direction == Direction.LEFT:
            new_position -= move.speed()

        if new_position < 0:
            raise ValueError("Position cannot be negative")

        self.position = new_position

class CharacterStatsManager:
    def __init__(self,
                 health: int = DEFAULT_HEALTH,
                 stamina: int = DEFAULT_STAMINA,
                 attacking_power: int = DEFAULT_ATTACK_POWER) -> None:
        self.health = health
        self.stamina = stamina
        self.attacking_power = attacking_power

    def decrease_stamina_by(self, decrease_amount: int):
        if decrease_amount > self.stamina:
            raise ValueError('decrease_amount must be less than stamina')
        self.stamina -= decrease_amount

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

    def calculate_attack_power(self, base_attack_power: int) -> int:
        attack_power = base_attack_power
        if self.claws:
            attack_power = self.claws.modify_attacking_power(attack_power)
        if self.teeth:
            attack_power = self.teeth.modify_attacking_power(attack_power)
        return attack_power

class Character:
    def __init__(self,
                 position_manager: PositionManager = PositionManager(),
                 stats_manager: CharacterStatsManager = CharacterStatsManager(),
                 appendage_manager: AppendageManager = AppendageManager()) -> None:
        self.position_manager = position_manager
        self.stats_manager = stats_manager
        self.appendage_manager = appendage_manager

    @property
    def stamina(self):
        return self.stats_manager.stamina

    @property
    def position(self) -> int:
        return self.position_manager.position

    @property
    def attack_power(self) -> int:
        return self.appendage_manager.calculate_attack_power(self.stats_manager.attacking_power)

    @property
    def health(self) -> int:
        return self.stats_manager.health

    @health.setter
    def health(self, value):
        self.stats_manager.health = value

    def get_possible_moves(self) -> List[Move]:
        return [move for move in [Crawl(), Hop(), Walk(), Run(), Fly()] if move.can_do(self)]

    def move(self, move: Move, direction: Direction):
        initial_position = self.position_manager.position
        initial_stamina = self.stats_manager.stamina

        try:
            self.position_manager.move(move, direction)
            self.stats_manager.decrease_stamina_by(move.uses_stamina())
        except Exception as e:
            self.position_manager.position = initial_position
            self.stats_manager.stamina = initial_stamina
            raise ValueError("Cannot make that move: {}".format(e))

    def attack(self, victim: 'Character') -> None:
        if victim.position != self.position:
            raise ValueError("Cant attack on the distance")
        victim.health -= self.attack_power

class CharacterBuilder:
    def __init__(self):
        self.position = DEFAULT_POSITION
        self.base_health = DEFAULT_HEALTH
        self.base_attack_power = DEFAULT_ATTACK_POWER
        self.base_stamina = DEFAULT_STAMINA
        self.legs = Legs()
        self.wings = Wings()
        self.claws = Claws()
        self.teeth = Teeth()

    def with_position(self, position: int) -> Self:
        self.position = position
        return self

    def with_health(self, base_health: int) -> Self:
        self.base_health = base_health
        return self

    def with_attack_power(self, base_attack_power: int) -> Self:
        self.base_attack_power = base_attack_power
        return self

    def with_stamina(self, base_stamina: int) -> Self:
        self.base_stamina = base_stamina
        return self

    def with_legs(self, count: int) -> Self:
        self.legs = Legs(count)
        return self

    def with_wings(self, count: int) -> Self:
        self.wings = Wings(count)
        return self

    def with_claws(self, level: int) -> Self:
        self.claws = Claws(level)
        return self

    def with_teeth(self, level: int) -> Self:
        self.teeth = Teeth(level)
        return self

    def build(self) -> Character:
        appendage_manager = AppendageManager(
            legs=self.legs,
            wings=self.wings,
            claws=self.claws,
            teeth=self.teeth
        )
        stats_manager = CharacterStatsManager(
            self.base_health,
            self.base_stamina,
            self.base_attack_power
        )
        return Character(
            position_manager=PositionManager(self.position),
            stats_manager=stats_manager,
            appendage_manager=appendage_manager
        )

