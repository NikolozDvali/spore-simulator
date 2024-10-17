from typing import Tuple


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

    def __getitem__(self, index: int) -> int:
        return self.coords[index]

    def to_tuple(self) -> Tuple[int, ...]:
        return self.coords
