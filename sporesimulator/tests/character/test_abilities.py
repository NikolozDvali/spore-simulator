import pytest

from sporesimulator.game.character.builder import CharacterBuilder
from sporesimulator.game.movement.move import Crawl, Direction, Hop, Walk, Run, Fly


def test_character_attack_character():
    attacker = CharacterBuilder().with_position(10).with_attack_power(10).build()
    victim = CharacterBuilder().with_position(10).with_health(100).build()

    attacker.attack(victim)
    assert victim.health == 90

def test_character_crawl_new_position():
    character = CharacterBuilder().with_position(10).with_stamina(1).build()
    character.move(Crawl, Direction.RIGHT)
    assert character.position == 11

def test_character_crawl_invalid_position():
    character = CharacterBuilder().with_position(0).with_stamina(1).build()
    with pytest.raises(ValueError):
        character.move(Crawl, Direction.LEFT)

def test_character_crawl_decreases_stamina():
    character = CharacterBuilder().with_position(10).with_stamina(1).build()
    character.move(Crawl, Direction.RIGHT)
    assert character.stamina == 0

def test_character_not_enough_stamina_to_crawl():
    character = CharacterBuilder().with_position(10).with_stamina(0).build()
    with pytest.raises(ValueError):
        character.move(Crawl, Direction.LEFT)

def test_character_not_enough_stamina_to_hop():
    character = CharacterBuilder().with_position(10).with_stamina(20).with_legs(1).build()
    with pytest.raises(ValueError):
        character.move(Hop, Direction.RIGHT)

def test_character_not_enough_stamina_to_walk():
    character = CharacterBuilder().with_position(10).with_stamina(40).with_legs(2).build()
    with pytest.raises(ValueError):
        character.move(Walk, Direction.RIGHT)

def test_character_not_enough_stamina_to_run():
    character = CharacterBuilder().with_position(10).with_stamina(60).with_legs(2).build()
    with pytest.raises(ValueError):
        character.move(Run, Direction.RIGHT)

def test_character_not_enough_stamina_to_fly():
    character = CharacterBuilder().with_position(10).with_stamina(80).with_wings(2).build()
    with pytest.raises(ValueError):
        character.move(Fly, Direction.RIGHT)

def test_character_can_crawl():
    character = CharacterBuilder().with_position(10).with_stamina(1).build()
    character.move(Crawl, Direction.RIGHT)
    assert character.position == 10 + Crawl.speed
    assert character.stamina == 1 - Crawl.uses_stamina

def test_character_can_hop():
    character = CharacterBuilder().with_position(10).with_stamina(21).with_legs(1).build()
    character.move(Hop, Direction.RIGHT)
    assert character.position == 10 + Hop.speed
    assert character.stamina == 21 - Hop.uses_stamina

def test_character_can_walk():
    character = CharacterBuilder().with_position(10).with_stamina(41).with_legs(2).build()
    character.move(Walk, Direction.RIGHT)
    assert character.position == 10 + Walk.speed
    assert character.stamina == 41 - Walk.uses_stamina

def test_character_can_run():
    character = CharacterBuilder().with_position(10).with_stamina(61).with_legs(2).build()
    character.move(Run, Direction.RIGHT)
    assert character.position == 10 + Run.speed
    assert character.stamina == 61 - Run.uses_stamina

def test_character_can_fly():
    character = CharacterBuilder().with_position(10).with_stamina(81).with_wings(2).build()
    character.move(Fly, Direction.RIGHT)
    assert character.position == 10 + Fly.speed
    assert character.stamina == 81 - Fly.uses_stamina

def test_character_possible_move_protocols_none():
    character = CharacterBuilder().with_stamina(0).build()
    assert character.get_available_move_protocols() == []

def test_character_possible_move_protocols_some():
    character = CharacterBuilder().with_stamina(50).with_legs(2).build()
    assert character.get_available_move_protocols() == [Crawl, Hop, Walk]

def test_character_possible_move_protocols_all_available():
    character = CharacterBuilder().with_stamina(100).with_legs(2).with_wings(2).build()
    assert character.get_available_move_protocols() == [Crawl, Hop, Walk, Run, Fly]
