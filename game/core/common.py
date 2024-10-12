from abc import ABC
from typing import Protocol


class Coordinate(Protocol):
    pass

class Coordinate1D(Coordinate):
    def __init__(self, x: int = 0):
        self.x = x

class Entity(ABC):
    def __init__(self, coordinate: Coordinate = Coordinate1D()) -> None:
        self.coordinate = coordinate

