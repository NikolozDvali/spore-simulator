import pytest

from sporesimulator.game.character.builder import CharacterBuilder


# """ATTACK"""

def test_character_attack_victim_somewhere_else():
    attacker = CharacterBuilder().with_position(10).with_attack_power(10).build()
    victim = CharacterBuilder().with_position(20).with_health(50).build()
    with pytest.raises(ValueError):
        attacker.attack(victim)


def test_character_attack_victim_decreases_victims_health():
    attacker = CharacterBuilder().with_position(10).with_attack_power(10).build()
    victim = CharacterBuilder().with_position(10).with_health(50).build()
    attacker.attack(victim)
    assert victim.health == 40
