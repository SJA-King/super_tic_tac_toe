from dataclasses import dataclass
from enum import Enum, auto


class Piece(Enum):
    Nought = auto()
    Cross = auto()
    Empty = auto()



@dataclass
class Position:
    row: int = None
    column: int = None


class Location:
    position: Position = None
    contains: Piece = None


class Grid:
    locations: {str}






class GameGrid:
    grids: {str, Grid} = None