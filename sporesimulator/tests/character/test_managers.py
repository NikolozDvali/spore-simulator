from sporesimulator.game.character.managers import AppendageManager, PositionManager, CharacterStatsManager
from sporesimulator.game.core.constants import DEFAULT_HEALTH, DEFAULT_STAMINA, DEFAULT_ATTACK_POWER


def test_empty_appendage_manager_str():
    appendage_manager = AppendageManager()
    assert str(appendage_manager) == "No appendages"


def test_non_empty_appendage_manager_str():
    appendage_manager = AppendageManager()
    appendage_manager.leg_count = 1
    appendage_manager.wing_count = 2
    appendage_manager.teeth_level = 3
    appendage_manager.claw_level = 4
    assert str(appendage_manager) == "1 legs, 2 wings, Teeth level: 3, Claw level: 4"


def test_some_appendages_appendage_manager_str():
    appendage_manager = AppendageManager()
    appendage_manager.leg_count = 1
    appendage_manager.claw_level = 4
    assert str(appendage_manager) == "1 legs, Claw level: 4"


def test_empty_position_manager_str():
    position_manager = PositionManager()
    assert str(position_manager) == "0"


def test_non_empty_position_manager_str():
    position_manager = PositionManager(15)
    assert str(position_manager) == "15"


def test_character_stats_manager_default_str():
    stats_manager = CharacterStatsManager()
    assert str(
        stats_manager) == f"Health: {DEFAULT_HEALTH}, Stamina: {DEFAULT_STAMINA}, Base Attack Power: {DEFAULT_ATTACK_POWER}"


def test_character_stats_manager_with_appendages_str():
    stats_manager = CharacterStatsManager()
    appendage_manager = AppendageManager()
    appendage_manager.claw_level = 5
    appendage_manager.teeth_level = 3
    expected_final_attack_power = stats_manager.calculate_attack_power(appendage_manager)
    assert stats_manager.str_with_appendages(appendage_manager) == (
        f"Health: {DEFAULT_HEALTH}, Stamina: {DEFAULT_STAMINA}, Base Attack Power: {DEFAULT_ATTACK_POWER}, "
        f"Final Attack Power: {expected_final_attack_power}")


def test_character_stats_manager_custom_values_str():
    stats_manager = CharacterStatsManager(health=150, stamina=120, base_attack_power=20)
    appendage_manager = AppendageManager()
    appendage_manager.claw_level = 5
    appendage_manager.teeth_level = 3
    expected_final_attack_power = stats_manager.calculate_attack_power(appendage_manager)
    assert stats_manager.str_with_appendages(appendage_manager) == (
        f"Health: 150, Stamina: 120, Base Attack Power: 20, "
        f"Final Attack Power: {expected_final_attack_power}")


def test_character_stats_manager_no_appendage_manager_str():
    stats_manager = CharacterStatsManager()
    assert str(stats_manager) == f"Health: {DEFAULT_HEALTH}, Stamina: {DEFAULT_STAMINA}, Base Attack Power: {DEFAULT_ATTACK_POWER}"
