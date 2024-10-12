
from game.character.characteristics import Legs, Wings, Claws, Teeth

class BaseCharacter:
    DEFAULT_BASE_ATTACK_POWER: int = 10
    DEFAULT_BASE_HEALTH: int = 100
    DEFAULT_BASE_STAMINA: int = 100

    def __init__(self, base_health: int, base_attack_power: int, base_stamina: int) -> None:
        self.health = base_health
        self.stamina = base_stamina
        self.__base_attack_power = base_attack_power

    @property
    def attack_power(self) -> int:
        return self.__base_attack_power


class Character(BaseCharacter):

    def __init__(self, base_health: int = BaseCharacter.DEFAULT_BASE_HEALTH,
                 base_attack_power: int = BaseCharacter.DEFAULT_BASE_ATTACK_POWER,
                 base_stamina: int = BaseCharacter.DEFAULT_BASE_STAMINA,
                 legs: Legs = Legs(),
                 wings: Wings = Wings(),
                 claws: Claws = Claws(),
                 teeth: Teeth = Teeth()) -> None:
        super().__init__(base_health, base_attack_power, base_stamina)
        self.legs = legs
        self.wings = wings
        self.claws = claws
        self.teeth = teeth

    @property
    def attack_power(self) -> int:
        return super().attack_power * self.claws.attacking_power_multiplier() + self.teeth.attacking_power_additional()
