from dataclasses import dataclass
from enum import Enum

class Direction(Enum):
    LEFT = -1
    RIGHT = 1

@dataclass
class Move:
    requires_stamina: int
    uses_stamina: int
    speed: int

@dataclass
class Crawl(Move):
    requires_stamina: int = 1
    uses_stamina: int = 1
    speed: int = 1
