from typing import Self

from sporesimulator.game.character.appendages import Legs, Wings, Claws, Teeth, AppendageManager
from sporesimulator.game.core.constants import DEFAULT_BASE_HEALTH, DEFAULT_BASE_ATTACK_POWER, DEFAULT_BASE_STAMINA


class Character:
    def __init__(self, base_health: int = DEFAULT_BASE_HEALTH,
                 base_attack_power: int = DEFAULT_BASE_ATTACK_POWER,
                 base_stamina: int = DEFAULT_BASE_STAMINA,
                 appendage_manager: AppendageManager | None = None) -> None:
        self.health = base_health
        self.stamina = base_stamina
        self.__base_attack_power = base_attack_power
        self.appendage_manager = appendage_manager if appendage_manager else AppendageManager()

    @property
    def attack_power(self) -> int:
        return self.appendage_manager.calculate_attack_power(self.__base_attack_power)


class CharacterBuilder:
    def __init__(self):
        self.base_health = DEFAULT_BASE_HEALTH
        self.base_attack_power = DEFAULT_BASE_ATTACK_POWER
        self.base_stamina = DEFAULT_BASE_STAMINA
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
        return Character(
            base_health=self.base_health,
            base_attack_power=self.base_attack_power,
            base_stamina=self.base_stamina,
            appendage_manager=appendage_manager
        )

