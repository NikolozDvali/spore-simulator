from game.core.common import Entity, Coordinate1D


def test_entity_default_coordinate():
    assert Entity().coordinate.to_tuple() == (0, )

def test_entity_update_position():
    entity = Entity()
    entity.update_position(Coordinate1D(3))
    assert entity.coordinate.to_tuple() == (3, )

