from typing import Self

from sporesimulator.game.character.appendages import Legs, Wings, Claws, Teeth, AppendageManager
from sporesimulator.game.core.constants import DEFAULT_HEALTH, DEFAULT_ATTACK_POWER, DEFAULT_STAMINA, DEFAULT_POSITION


class CharacterStatsManager:
    def __init__(self,
                 health: int = DEFAULT_HEALTH,
                 stamina: int = DEFAULT_STAMINA,
                 attacking_power: int = DEFAULT_ATTACK_POWER) -> None:
        self.health = health
        self.stamina = stamina
        self.attacking_power = attacking_power

class Character:
    def __init__(self,
                 position: int = 0,
                 stats_manager: CharacterStatsManager | None = None,
                 appendage_manager: AppendageManager | None = None) -> None:
        self.position = position
        self.stats_manager = stats_manager
        self.appendage_manager = appendage_manager if appendage_manager else AppendageManager()

    @property
    def attack_power(self) -> int:
        return self.appendage_manager.calculate_attack_power(self.stats_manager.attacking_power)

    @property
    def health(self) -> int:
        return self.stats_manager.health

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

    def with_base_health(self, base_health: int) -> Self:
        self.base_health = base_health
        return self

    def with_base_attack_power(self, base_attack_power: int) -> Self:
        self.base_attack_power = base_attack_power
        return self

    def with_base_stamina(self, base_stamina: int) -> Self:
        self.base_stamina = base_stamina
        return self

    def with_legs(self, legs: Legs) -> Self:
        self.legs = legs
        return self

    def with_wings(self, wings: Wings) -> Self:
        self.wings = wings
        return self

    def with_claws(self, claws: Claws) -> Self:
        self.claws = claws
        return self

    def with_teeth(self, teeth: Teeth) -> Self:
        self.teeth = teeth
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
            position=self.position,
            stats_manager=stats_manager,
            appendage_manager=appendage_manager
        )

