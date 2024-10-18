from sporesimulator.game.character.builder import CharacterBuilder


def test_character_attack_character():
    attacker = CharacterBuilder().with_position(10).with_attack_power(10).build()
    victim = CharacterBuilder().with_position(10).with_health(100).build()

    attacker.attack(victim)
    assert victim.health == 90