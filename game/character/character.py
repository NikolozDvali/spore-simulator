from abc import ABC

from game.character.characteristics import Legs, Wings, Claws, Teeth
from game.world.world import Coordinate, Coordinate1D
from dataclasses import dataclass

@dataclass
class CharacterConfig:
    base_health: int = 100
    base_attack_power: int = 10
    base_stamina: int = 100
    legs: Legs = Legs()
    wings: Wings = Wings()
    claws: Claws = Claws()
    teeth: Teeth = Teeth()

class Entity(ABC):
    def __init__(self, coordinate: Coordinate = Coordinate1D()) -> None:
        self.coordinate = coordinate

class BaseCharacter(Entity):
    def __init__(self, base_health: int, base_attack_power: int, base_stamina: int) -> None:
        super().__init__()
        self.health = base_health
        self.stamina = base_stamina
        self.__base_attack_power = base_attack_power

    @property
    def attack_power(self) -> int:
        return self.__base_attack_power

class Character(BaseCharacter):
    def __init__(self, character_config: CharacterConfig = CharacterConfig()) -> None:
        super().__init__(character_config.base_health, character_config.base_attack_power, character_config.base_stamina)
        self.legs = character_config.legs
        self.wings = character_config.wings
        self.claws = character_config.claws
        self.teeth = character_config.teeth

    @property
    def attack_power(self) -> int:
        return super().attack_power * self.claws.attacking_power_multiplier() + self.teeth.attacking_power_additional()
