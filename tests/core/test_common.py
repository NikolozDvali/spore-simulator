from game.core.common import Entity, Coordinate

def test_coordinate_equality():
    assert Coordinate(1, 2) == Coordinate(1, 2)
    assert Coordinate(1, 2) != Coordinate(2, 1)

def test_entity_default_coordinate():
    assert Entity().coordinate.to_tuple() == (0, )

def test_entity_update_position():
    entity = Entity()
    entity.update_position(Coordinate(3))
    assert entity.coordinate.to_tuple() == (3, )

