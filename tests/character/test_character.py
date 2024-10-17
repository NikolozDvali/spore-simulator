from game.character.character import CharacterBuilder


def test_default_character_characteristics():
    character = CharacterBuilder().build()

    assert character.legs.count == 0
    assert character.wings.count == 0
    assert character.claws.level == 0
    assert character.teeth.level == 0



