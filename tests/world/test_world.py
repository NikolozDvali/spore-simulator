from unittest.mock import MagicMock

import pytest

from game.core.common import Entity, Coordinate
from game.world.world import World


def test_default_world_is_empty():
    assert len(World().entities) == 0

def test_world_with_a_single_entity():
    world = World()
    mock_entity: Entity = MagicMock(spec=Entity)
    world.add_entity(mock_entity)

    assert len(world.entities) == 1

def test_world_get_entity_position():
    world = World()
    mock_entity: Entity = MagicMock(spec=Entity)
    mock_entity.coordinate = (0, 0, 0)
    world.add_entity(mock_entity)

    assert world.get_entity_position(mock_entity) == (0, 0, 0)

def test_world_get_entity_position_invalid():
    world = World()
    mock_entity: Entity = MagicMock(spec=Entity)
    mock_entity.coordinate = (0, 0, 0)

    with pytest.raises(ValueError):
        world.get_entity_position(mock_entity)

def test_world_get_entities_at_position():
    world = World()
    mock_entity_1: Entity = MagicMock(spec=Entity)
    mock_entity_2: Entity = MagicMock(spec=Entity)
    mock_entity_1.coordinate = Coordinate(0, 12, 0)
    mock_entity_2.coordinate = Coordinate(0, 12, 0)
    world.add_entity(mock_entity_1)
    world.add_entity(mock_entity_2)

    assert world.get_entities_at_position(Coordinate(0, 12, 0)) == [mock_entity_1, mock_entity_2]
