from game.world.world import World


def test_default_world_is_empty():
    assert len(World().entities) == 0