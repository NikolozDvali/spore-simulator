from game.character.characteristics import Legs, Wings, Claws, Teeth


class Character:
    DEFAULT_BASE_ATTACK_POWER: int = 10
    DEFAULT_BASE_HEALTH: int = 100
    DEFAULT_BASE_STAMINA: int = 100

    def __init__(self, base_health: int = DEFAULT_BASE_HEALTH,
                 base_attack_power: int = DEFAULT_BASE_ATTACK_POWER,
                 base_stamina: int = DEFAULT_BASE_STAMINA,
                 legs: Legs = Legs(),
                 wings: Wings = Wings(),
                 claws: Claws = Claws(),
                 teeth: Teeth = Teeth()) -> None:
        self.legs = legs
        self.wings = wings
        self.claws = claws
        self.teeth = teeth

        self.health = base_health
        self.stamina = base_stamina
        self.__base_attack_power = base_attack_power

    @property
    def attack_power(self) -> int:
        return self.__base_attack_power * self.claws.attacking_power_multiplier() + self.teeth.attacking_power_additional()
