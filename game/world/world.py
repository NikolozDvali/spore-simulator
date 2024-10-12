from abc import abstractmethod, ABC
from typing import Set, List

from game.core.common import Entity, Coordinate

class World(ABC):
    def __init__(self):
        self.entities: List[Entity] = []

    def get_entities(self) -> List[Entity]:
        return self.entities

    @abstractmethod
    def add_entity(self, entity: Entity):
        pass

    @abstractmethod
    def move_entity(self, entity: Entity, move_to: Coordinate):
        pass

    @abstractmethod
    def get_entities_at_coordinate(self, coordinate: Coordinate) -> List[Entity]:
        pass

    @abstractmethod
    def remove_entity(self, entity: Entity):
        pass

class LowerBounded1DWorld(World):
    def __init__(self, lower_bound: int = 0):
        super().__init__()
        self.lower_bound = lower_bound

    def add_entity(self, entity: Entity):
        if entity in self.entities:
            raise ValueError(f'Entity {entity} already in the world')
        if entity.coordinate[0] < self.lower_bound:
            raise ValueError(f'Coordinate {entity.coordinate[0]} < {self.lower_bound}')
        self.entities.append(entity)

    def remove_entity(self, entity: Entity):
        if entity not in self.entities:
            raise ValueError(f'Entity {entity} not in world')
        self.entities.remove(entity)

    def move_entity(self, entity: Entity, new_coordinate: Coordinate):
        if entity not in self.entities:
            raise ValueError(f'Entity {entity} not in world world')
        if new_coordinate[0] < self.lower_bound:
            raise ValueError(f'Entity {entity} is below the lower bound')
        entity.coordinate = new_coordinate

    def get_entities_at_coordinate(self, coordinate: Coordinate) -> List[Entity]:
        return [entity for entity in self.entities if entity.coordinate == coordinate]