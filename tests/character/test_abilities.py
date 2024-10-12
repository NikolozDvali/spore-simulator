from unittest.mock import MagicMock

from game.character.abilities import can_crawl, can_hop, can_run, can_walk, can_fly, check_ability, \
    get_possible_move_methods, MoveMethod
from game.character.character import Character
from game.character.characteristics import Wings, Legs

def test_crawl():
    assert check_ability(can_crawl, Character()) is True
    assert check_ability(can_crawl, Character(base_stamina=0)) is False

def test_can_hop():
    character = Character()
    mocked_legs: Legs = MagicMock(spec=Legs)
    character.legs = mocked_legs

    character.legs.can_hop.return_value = False
    assert check_ability(can_hop, character) is False

    character.legs.can_hop.return_value = True
    character.stamina = 20
    assert check_ability(can_hop, character) is False

    character.stamina = 21
    assert check_ability(can_hop, character) is True

def test_can_walk():
    character = Character()
    mocked_legs: Legs = MagicMock(spec=Legs)
    character.legs = mocked_legs

    character.legs.can_walk.return_value = False
    assert check_ability(can_walk, character) is False

    character.legs.can_walk.return_value = True
    character.stamina = 40
    assert check_ability(can_walk, character) is False

    character.stamina = 41
    assert check_ability(can_walk, character) is True

def test_can_run():
    character = Character()
    mocked_legs: Legs = MagicMock(spec=Legs)
    character.legs = mocked_legs

    character.legs.can_run.return_value = False
    assert check_ability(can_run, character) is False

    character.legs.can_run.return_value = True
    character.stamina = 60
    assert check_ability(can_run, character) is False

    character.stamina = 61
    assert check_ability(can_run, character) is True

def test_can_fly():
    character = Character()
    mocked_wings: Wings = MagicMock(spec=Wings)
    character.wings = mocked_wings

    character.wings.can_fly.return_value = False
    assert check_ability(can_fly, character) is False

    character.wings.can_fly.return_value = True
    character.stamina = 80
    assert check_ability(can_fly, character) is False

    character.stamina = 81
    assert check_ability(can_fly, character) is True

def test_move_abilities():
    assert get_possible_move_methods(Character(base_stamina=0)) == []

    character = Character(base_stamina=Character.DEFAULT_BASE_STAMINA)
    mocked_legs: Legs = MagicMock(spec=Legs)
    character.legs = mocked_legs
    mocked_wings: Wings = MagicMock(spec=Wings)
    character.wings = mocked_wings

    character.legs.can_hop.return_value = True
    character.legs.can_walk.return_value = True
    character.legs.can_run.return_value = True
    character.wings.can_fly.return_value = True

    assert get_possible_move_methods(character) == [MoveMethod.CRAWL, MoveMethod.HOP, MoveMethod.WALK, MoveMethod.RUN, MoveMethod.FLY]

