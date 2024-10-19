import pytest

from game.character.builder import CharacterBuilder
from game.movement.move import MovementAgent
from game.process.game_config import GameConfig


@pytest.fixture
def game_config():
    predator = CharacterBuilder().with_name("Predator").build()
    prey = CharacterBuilder().with_name("Prey").build()
    return GameConfig(predator, prey)


def test_initialization(game_config):
    assert game_config.predator.name == "Predator"
    assert game_config.prey.name == "Prey"
    assert isinstance(game_config.predator_movement_agent, MovementAgent)


def test_set_predator(game_config):
    new_predator = CharacterBuilder().with_name("New Predator").build()
    game_config.set_predator(new_predator)
    assert game_config.predator.name == "New Predator"


def test_set_prey(game_config):
    new_prey = CharacterBuilder().with_name("New Prey").build()
    game_config.set_prey(new_prey)
    assert game_config.prey.name == "New Prey"
