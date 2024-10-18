import pytest

from sporesimulator.game.character.builder import CharacterBuilder
from sporesimulator.game.move.move import Crawl, Direction


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