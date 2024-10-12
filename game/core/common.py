from abc import ABC
from typing import Protocol, Tuple


class Coordinate(Protocol):
    def to_tuple(self) -> Tuple[int, ...]:
        pass

class Coordinate1D(Coordinate):
    def __init__(self, x: int = 0):
        self.x = x

    def to_tuple(self) -> Tuple[int, ...]:
        return (self.x,)

class Entity(ABC):
    def __init__(self, coordinate: Coordinate = Coordinate1D()) -> None:
        self.coordinate = coordinate

    def update_position(self, new_position: Coordinate) -> None:
        self.coordinate = new_position


