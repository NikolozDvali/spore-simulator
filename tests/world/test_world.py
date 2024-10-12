from unittest.mock import MagicMock

import pytest

from game.core.common import Entity, Coordinate
from game.world.world import LowerBounded1DWorld


def test_empty_limited_1d_world_entities():
    assert LowerBounded1DWorld().entities == []

def test_add_valid_entity():
    mock_entity: Entity = MagicMock(spec=Entity)
    mock_coordinate: Coordinate = MagicMock(spec=Coordinate)
    mock_coordinate.__getitem__.side_effect = lambda index: 0 if index == 0 else None
    mock_entity.coordinate = mock_coordinate

    world = LowerBounded1DWorld()
    world.add_entity(mock_entity)
    assert len(world.entities) == 1

def test_add_invalid_coordinate_entity():
    mock_entity: Entity = MagicMock(spec=Entity)
    mock_coordinate: Coordinate = MagicMock(spec=Coordinate)
    mock_coordinate.__getitem__.side_effect = lambda index: -1 if index == 0 else None
    mock_entity.coordinate = mock_coordinate

    world = LowerBounded1DWorld()
    with pytest.raises(ValueError):
        world.add_entity(mock_entity)

def test_add_entity_twice():
    mock_entity: Entity = MagicMock(spec=Entity)
    mock_coordinate: Coordinate = MagicMock(spec=Coordinate)
    mock_coordinate.__getitem__.side_effect = lambda index: 0 if index == 0 else None
    mock_entity.coordinate = mock_coordinate

    world = LowerBounded1DWorld()
    world.add_entity(mock_entity)
    with pytest.raises(ValueError):
        world.add_entity(mock_entity)

def test_remove_existing_entity():
    mock_entity: Entity = MagicMock(spec=Entity)
    mock_coordinate: Coordinate = MagicMock(spec=Coordinate)
    mock_coordinate.__getitem__.side_effect = lambda index: 0 if index == 0 else None
    mock_entity.coordinate = mock_coordinate

    world = LowerBounded1DWorld()
    world.add_entity(mock_entity)
    world.remove_entity(mock_entity)
    assert len(world.entities) == 0

def test_remove_non_existing_entity():
    mock_entity: Entity = MagicMock(spec=Entity)
    mock_coordinate: Coordinate = MagicMock(spec=Coordinate)
    mock_coordinate.__getitem__.side_effect = lambda index: 0 if index == 0 else None
    mock_entity.coordinate = mock_coordinate

    world = LowerBounded1DWorld()
    with pytest.raises(ValueError):
        world.remove_entity(mock_entity)

def test_remove_entity_twice():
    mock_entity: Entity = MagicMock(spec=Entity)
    mock_coordinate: Coordinate = MagicMock(spec=Coordinate)
    mock_coordinate.__getitem__.side_effect = lambda index: 0 if index == 0 else None
    mock_entity.coordinate = mock_coordinate

    world = LowerBounded1DWorld()
    world.add_entity(mock_entity)
    world.remove_entity(mock_entity)
    with pytest.raises(ValueError):
        world.remove_entity(mock_entity)

def test_move_existing_entity_to_valid_coordinate():
    mock_entity: Entity = MagicMock(spec=Entity)
    mock_coordinate: Coordinate = MagicMock(spec=Coordinate)
    mock_coordinate.__getitem__.side_effect = lambda index: 0 if index == 0 else None
    mock_entity.coordinate = mock_coordinate

    world = LowerBounded1DWorld()
    world.add_entity(mock_entity)

    mock_new_coordinate: Coordinate = MagicMock(spec=Coordinate)
    mock_new_coordinate.__getitem__.side_effect = lambda index: 2 if index == 0 else None

    world.move_entity(mock_entity, mock_new_coordinate)
    assert len(world.entities) == 1

def test_move_existing_entity_to_invalid_coordinate():
    mock_entity: Entity = MagicMock(spec=Entity)
    mock_coordinate: Coordinate = MagicMock(spec=Coordinate)
    mock_coordinate.__getitem__.side_effect = lambda index: 0 if index == 0 else None
    mock_entity.coordinate = mock_coordinate

    world = LowerBounded1DWorld()
    world.add_entity(mock_entity)

    mock_new_coordinate: Coordinate = MagicMock(spec=Coordinate)
    mock_new_coordinate.__getitem__.side_effect = lambda index: -1 if index == 0 else None

    with pytest.raises(ValueError):
        world.move_entity(mock_entity, mock_new_coordinate)

def test_move_non_existing_entity():
    mock_entity: Entity = MagicMock(spec=Entity)
    mock_coordinate: Coordinate = MagicMock(spec=Coordinate)
    mock_coordinate.__getitem__.side_effect = lambda index: 0 if index == 0 else None
    mock_entity.coordinate = mock_coordinate

    world = LowerBounded1DWorld()
    with pytest.raises(ValueError):
        world.move_entity(mock_entity, mock_coordinate)

def test_no_entities_at_coordinate():
    world = LowerBounded1DWorld()
    mock_coordinate: Coordinate = MagicMock(spec=Coordinate)
    mock_coordinate.__getitem__.side_effect = lambda index: 0 if index == 0 else None

    assert world.get_entities_at_coordinate(mock_coordinate) == []

def test_a_single_entity_at_coordinate():
    mock_entity: Entity = MagicMock(spec=Entity)
    mock_coordinate: Coordinate = MagicMock(spec=Coordinate)
    mock_coordinate.__getitem__.side_effect = lambda index: 0 if index == 0 else None
    mock_entity.coordinate = mock_coordinate

    world = LowerBounded1DWorld()
    world.add_entity(mock_entity)
    assert world.get_entities_at_coordinate(mock_coordinate) == [mock_entity]

def test_multiple_entities_at_coordinate():
    mock_entity1: Entity = MagicMock(spec=Entity)
    mock_entity2: Entity = MagicMock(spec=Entity)
    mock_coordinate: Coordinate = MagicMock(spec=Coordinate)
    mock_coordinate.__getitem__.side_effect = lambda index: 0 if index == 0 else None
    mock_entity1.coordinate = mock_coordinate
    mock_entity2.coordinate = mock_coordinate

    world = LowerBounded1DWorld()
    world.add_entity(mock_entity1)
    world.add_entity(mock_entity2)
    assert world.get_entities_at_coordinate(mock_coordinate) == [mock_entity1, mock_entity2]