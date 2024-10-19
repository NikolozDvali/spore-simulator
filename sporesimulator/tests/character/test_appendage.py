import pytest

from sporesimulator.game.character.appendages import Legs, Wings, Claws, Teeth

"""=========================LEGS============================="""


def test_default_legs():
    assert Legs().count == 0


def test_custom_number_of_legs():
    assert Legs(10).count == 10


def test_evolve_legs():
    legs = Legs(2)
    legs.evolve(5)
    assert legs.count == 7


def test_negative_legs():
    with pytest.raises(ValueError):
        Legs(-1)


def test_can_hop():
    assert Legs().can_hop() is False
    assert Legs(1).can_hop() is True


def test_can_walk():
    assert Legs(1).can_walk() is False
    assert Legs(2).can_walk() is True


def test_can_run():
    assert Legs(1).can_run() is False
    assert Legs(2).can_run() is True


"""=========================WINGS============================="""


def test_default_wings():
    assert Wings().count == 0


def test_custom_number_of_wings():
    assert Wings(10).count == 10


def test_evolve_wings():
    wings = Wings(2)
    wings.evolve(5)
    assert wings.count == 7


def test_negative_wings():
    with pytest.raises(ValueError):
        Wings(-1)


def test_can_fly():
    assert Wings(1).can_fly() is False
    assert Wings(2).can_fly() is True


"""=========================CLAWS============================="""


def test_default_claws():
    assert Claws().level == 0


def test_custom_size_of_claws():
    assert Claws(1).level == 1
    assert Claws(2).level == 2


def test_negative_size():
    with pytest.raises(ValueError):
        Claws(-1)


def test_evolve_claws():
    claws = Claws()
    claws.evolve()
    assert claws.level == 1


def test_attacking_power_multiplier():
    assert Claws().modify_attacking_power(100) == 100
    assert Claws(1).modify_attacking_power(100) == 200
    assert Claws(2).modify_attacking_power(100) == 300
    assert Claws(3).modify_attacking_power(100) == 400
    assert Claws(4).modify_attacking_power(100) == 400


"""=========================TEETH============================="""


def test_default_teeth():
    assert Teeth().level == 0


def test_custom_sharpness_of_teeth():
    assert Teeth(1).level == 1
    assert Teeth(2).level == 2


def test_negative_sharpness():
    with pytest.raises(ValueError):
        Teeth(-1)


def test_evolve_teeth():
    teeth = Teeth()
    teeth.evolve()
    assert teeth.level == 1


def test_attacking_power_additional():
    assert Teeth().modify_attacking_power(100) == 100
    assert Teeth(1).modify_attacking_power(100) == 103
    assert Teeth(2).modify_attacking_power(100) == 106
    assert Teeth(3).modify_attacking_power(100) == 109
    assert Teeth(4).modify_attacking_power(100) == 109
