from abc import ABC
from dataclasses import dataclass
from enum import Enum
from typing import Protocol, List, runtime_checkable


class Direction(Enum):
    LEFT = -1
    NOWHERE = 0
    RIGHT = 1

@dataclass
class Move(ABC):
    requires_stamina: int
    uses_stamina: int
    speed: int


@dataclass
class Crawl(Move):
    requires_stamina: int = 1
    uses_stamina: int = 1
    speed: int = 1


@dataclass
class Hop(Move):
    requires_stamina: int = 21
    uses_stamina: int = 2
    speed: int = 3


@dataclass
class Walk(Move):
    requires_stamina: int = 41
    uses_stamina: int = 2
    speed: int = 4

@dataclass
class Run(Move):
    requires_stamina: int = 61
    uses_stamina: int = 4
    speed: int = 6


@dataclass
class Fly(Move):
    requires_stamina: int = 81
    uses_stamina: int = 4
    speed: int = 8

@runtime_checkable
class MovementAgent(Protocol):
    def next_move(self, possible_moves: List[type[Move]]) -> type[Move] | None:
        pass

class GreedyMovementAgent(MovementAgent):
    def next_move(self, possible_moves: List[type[Move]]) -> type[Move] | None:
        if not possible_moves:
            return None
        return max(possible_moves, key=lambda move: move.speed)