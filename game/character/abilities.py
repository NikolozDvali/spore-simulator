from typing import Callable

from game.character.character import Character

AbilityFunction = Callable[[Character], bool]

def check_ability(ability: AbilityFunction, character: Character) -> bool:
    return ability(character)

def can_crawl(character: Character) -> bool:
    return character.stamina > 0

def can_hop(character: Character) -> bool:
    return character.legs.can_hop() and character.stamina > 20

def can_walk(character: Character) -> bool:
    return character.legs.can_walk() and character.stamina > 40

def can_run(character: Character) -> bool:
    return character.legs.can_run() and character.stamina > 60

def can_fly(character: Character) -> bool:
    return character.wings.can_fly() and character.stamina > 80