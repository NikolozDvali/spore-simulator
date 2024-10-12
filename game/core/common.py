from abc import ABC
from typing import Protocol, Tuple


class Coordinate:
    def __init__(self, *coords: int) -> None:
        if not coords:
            self.coords = (0,)
        else:
            self.coords = coords

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Coordinate):
            return self.coords == other.coords
        return False

    def __str__(self) -> str:
        return str(self.coords)

    def to_tuple(self) -> Tuple[int, ...]:
        return self.coords

    def __getitem__(self, index: int) -> int:
        return self.coords[index]

class Entity(ABC):
    def __init__(self, coordinate: Coordinate = Coordinate()) -> None:
        self.coordinate = coordinate

    def update_position(self, new_position: Coordinate) -> None:
        self.coordinate = new_position


