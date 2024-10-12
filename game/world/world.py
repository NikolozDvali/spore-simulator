from typing import Protocol


class Coordinate(Protocol):
    pass

class Coordinate1D(Coordinate):
    def __init__(self, x: int = 0):
        self.x = x
