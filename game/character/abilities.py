from enum import Enum
from typing import Callable, List

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

class MoveMethod(Enum):
    CRAWL = "crawl"
    HOP = "hop"
    WALK = "walk"
    RUN = "run"
    FLY = "fly"

def get_possible_move_methods(character: Character) -> List[MoveMethod]:
    possible_moves = []

    if check_ability(can_crawl, character):
        possible_moves.append(MoveMethod.CRAWL)
    if check_ability(can_hop, character):
        possible_moves.append(MoveMethod.HOP)
    if check_ability(can_walk, character):
        possible_moves.append(MoveMethod.WALK)
    if check_ability(can_run, character):
        possible_moves.append(MoveMethod.RUN)
    if check_ability(can_fly, character):
        possible_moves.append(MoveMethod.FLY)

    return possible_moves