from typing import Self

from game.character.appendages import Legs, Wings, Claws, Teeth

class Character:
    def __init__(self, base_health: int = 100, base_attack_power: int = 10, base_stamina: int = 100,
                 legs: Legs = None, wings: Wings = None, claws: Claws = None, teeth: Teeth = None) -> None:
        self.health = base_health
        self.stamina = base_stamina
        self.__base_attack_power = base_attack_power
        self.legs = legs if legs is not None else Legs()
        self.wings = wings if wings is not None else Wings()
        self.claws = claws if claws is not None else Claws()
        self.teeth = teeth if teeth is not None else Teeth()

    @property
    def attack_power(self) -> int:
        attack_power = self.__base_attack_power
        if self.teeth:
            attack_power = self.teeth.modify_attacking_power(attack_power)
        if self.claws:
            attack_power = self.claws.modify_attacking_power(attack_power)
        return attack_power

class CharacterBuilder:
    def __init__(self):
        self.base_health = 100
        self.base_attack_power = 10
        self.base_stamina = 50
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
        return Character(
            base_health=self.base_health,
            base_attack_power=self.base_attack_power,
            base_stamina=self.base_stamina,
            legs=self.legs,
            wings=self.wings,
            claws=self.claws,
            teeth=self.teeth
        )
