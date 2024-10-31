import pytest

from game.character.appendages import Legs, Wings, Claws, Teeth

"""=========================LEGS============================="""


def test_default_legs() -> None:
    assert Legs().count == 0


def test_custom_number_of_legs() -> None:
    assert Legs(10).count == 10


def test_evolve_legs() -> None:
    legs = Legs(2)
    legs.evolve(5)
    assert legs.count == 7


def test_negative_legs() -> None:
    with pytest.raises(ValueError):
        Legs(-1)


def test_can_hop() -> None:
    assert Legs().can_hop() is False
    assert Legs(1).can_hop() is True


def test_can_walk() -> None:
    assert Legs(1).can_walk() is False
    assert Legs(2).can_walk() is True


def test_can_run() -> None:
    assert Legs(1).can_run() is False
    assert Legs(2).can_run() is True


"""=========================WINGS============================="""


def test_default_wings() -> None:
    assert Wings().count == 0


def test_custom_number_of_wings() -> None:
    assert Wings(10).count == 10


def test_evolve_wings() -> None:
    wings = Wings(2)
    wings.evolve(5)
    assert wings.count == 7


def test_negative_wings() -> None:
    with pytest.raises(ValueError):
        Wings(-1)


def test_can_fly() -> None:
    assert Wings(1).can_fly() is False
    assert Wings(2).can_fly() is True


"""=========================CLAWS============================="""


def test_default_claws() -> None:
    assert Claws().level == 0


def test_custom_size_of_claws() -> None:
    assert Claws(1).level == 1
    assert Claws(2).level == 2


def test_negative_size() -> None:
    with pytest.raises(ValueError):
        Claws(-1)


def test_evolve_claws() -> None:
    claws = Claws()
    claws.evolve()
    assert claws.level == 1


def test_attacking_power_multiplier() -> None:
    assert Claws().modify_attacking_power(100) == 100
    assert Claws(1).modify_attacking_power(100) == 200
    assert Claws(2).modify_attacking_power(100) == 300
    assert Claws(3).modify_attacking_power(100) == 400
    assert Claws(4).modify_attacking_power(100) == 400


"""=========================TEETH============================="""


def test_default_teeth() -> None:
    assert Teeth().level == 0


def test_custom_sharpness_of_teeth() -> None:
    assert Teeth(1).level == 1
    assert Teeth(2).level == 2


def test_negative_sharpness() -> None:
    with pytest.raises(ValueError):
        Teeth(-1)


def test_evolve_teeth() -> None:
    teeth = Teeth()
    teeth.evolve()
    assert teeth.level == 1


def test_attacking_power_additional() -> None:
    assert Teeth().modify_attacking_power(100) == 100
    assert Teeth(1).modify_attacking_power(100) == 103
    assert Teeth(2).modify_attacking_power(100) == 106
    assert Teeth(3).modify_attacking_power(100) == 109
    assert Teeth(4).modify_attacking_power(100) == 109
