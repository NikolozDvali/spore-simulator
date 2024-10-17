import pytest

from sporesimulator.game.character.character import CharacterBuilder, Crawl, Fly, Run, Walk, Hop, Direction


def test_default_character_possible_moves():
    character = CharacterBuilder().build()
    assert character.get_possible_moves() == [Crawl()]


def test_all_mighty_character_possible_moves():
    character = (CharacterBuilder()
                 .with_legs(4)
                 .with_wings(2)
                 .with_stamina(100)
                 .build())
    assert character.get_possible_moves() == [Crawl(), Hop(), Walk(), Run(), Fly()]

    """POSITION CHANGE DURING MOVE"""

def test_character_crawl_right_position_change():
    character = CharacterBuilder().with_position(100).build()
    character.move(Crawl(), Direction.RIGHT)
    assert character.position == 101

def test_character_crawl_left_position_change():
    character = CharacterBuilder().with_position(100).build()
    character.move(Crawl(), Direction.LEFT)
    assert character.position == 99

def test_character_hop_right_position_change():
    character = CharacterBuilder().with_legs(1).with_position(100).build()
    character.move(Hop(), Direction.RIGHT)
    assert character.position == 103

def test_character_walk_right_position_change():
    character = CharacterBuilder().with_legs(2).with_position(100).build()
    character.move(Walk(), Direction.RIGHT)
    assert character.position == 104

def test_character_run_right_position_change():
    character = CharacterBuilder().with_legs(2).with_position(100).build()
    character.move(Run(), Direction.RIGHT)
    assert character.position == 106

def test_character_fly_right_position_change():
    character = CharacterBuilder().with_wings(2).with_position(100).build()
    character.move(Fly(), Direction.RIGHT)
    assert character.position == 108

def test_character_invalid_move():
    character = CharacterBuilder().with_legs(1).with_position(5).build()
    with pytest.raises(ValueError):
        character.move(Fly(), Direction.LEFT)

    # """STAMINA CHANGE DURING MOVE"""