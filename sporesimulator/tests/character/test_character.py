from sporesimulator.game.character.character import CharacterBuilder, Crawl, Fly, Run, Walk, Hop, Direction


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

def test_character_crawl_right_position_change():
    character = CharacterBuilder().with_position(100).build()
    character.move(Crawl(), Direction.RIGHT)
    assert character.position == 101

def test_character_crawl_left_position_change():
    character = CharacterBuilder().with_position(100).build()
    character.move(Crawl(), Direction.LEFT)
    assert character.position == 99