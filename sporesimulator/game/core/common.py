from abc import ABC, abstractmethod


class Entity(ABC):
    pass

class Ability(ABC):
    @abstractmethod
    def requires_stamina(self) -> int:
        pass

    @abstractmethod
    def uses_stamina(self) -> int:
        pass

    def __eq__(self, other: object):
        return isinstance(other, Ability)

class Appendage(ABC):
    def __init__(self, attribute: int = 0):
        if attribute < 0:
            raise ValueError("Attribute value cannot be negative")
        self.attribute = attribute

    def evolve(self, increment: int = 1):
        self.attribute += increment

    def modify_attacking_power(self, attacking_power: int):
        pass