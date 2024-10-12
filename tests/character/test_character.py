from unittest.mock import MagicMock

from game.character.character import Character
from game.character.characteristics import Claws, Teeth, Legs


def test_default_character_characteristics():
    character = Character()

    assert character.legs.count == 0
    assert character.wings.count == 0
    assert character.claws.level == 0
    assert character.teeth.level == 0

def test_default_character_metrics():
    character = Character()
    assert character.attack_power == Character.DEFAULT_BASE_ATTACK_POWER
    assert character.health == Character.DEFAULT_BASE_HEALTH
    assert character.stamina == Character.DEFAULT_BASE_STAMINA

def test_character_attacking_power_calculation():
    mock_claws = MagicMock(spec=Claws)
    mock_claws.attacking_power_multiplier.return_value = 20

    mock_teeth = MagicMock(spec=Teeth)
    mock_teeth.attacking_power_additional.return_value = 20

    character = Character(claws=mock_claws, teeth=mock_teeth)

    expected_attacking_power = Character.DEFAULT_BASE_ATTACK_POWER * mock_claws.attacking_power_multiplier() + mock_teeth.attacking_power_additional()

    assert character.attack_power == expected_attacking_power



