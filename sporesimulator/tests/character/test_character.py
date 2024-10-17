from sporesimulator.game.character.character import CharacterBuilder, Crawl, Fly, Run, Walk, Hop


def test_default_character_possible_moves():
    character = CharacterBuilder().build()
    assert character.get_possible_moves() == [Crawl()]


def test_all_mighty_character_possible_moves():
    character = (CharacterBuilder()
                 .with_legs(4)
                 .with_wings(2)
                 .with_stamina(100)
                 .build())
    assert character.get_possible_moves() == [Crawl(), Hop(), Walk(), Run(), Fly()]
