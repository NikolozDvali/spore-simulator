from typing import Set, List

from game.core.common import Entity, Coordinate


class World:
    def __init__(self):
        self.entities: Set[Entity] = set()

    def add_entity(self, entity: Entity):
        self.entities.add(entity)

    def get_entity_position(self, entity: Entity) -> Coordinate:
        if entity in self.entities:
            return entity.coordinate
        else:
            raise ValueError("Entity not found in the world.")

    def get_entities_at_position(self, coordinate: Coordinate) -> List[Entity]:
        return [entity for entity in self.entities if entity.coordinate == coordinate]