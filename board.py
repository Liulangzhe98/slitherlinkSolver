from enum import Enum
from itertools import zip_longest as zip_l
import random
from typing import List, Sequence


symbols = dict(
    SE='╔', SW='╗',
    NE='╚', NW='╝',
    NS='║', WE='═',
)


class Vert(Enum):
    TAKEN = '║'
    TAKEN_FLAT = '═════'
    FREE  = ' '
    FREE_FLAT = '     '
    NOT   = '|' # TODO: Find better ascii
    NOT_FLAT = '-----'



class Side(Enum):
    north = 0
    east  = 1
    south = 2
    west  = 3


class Cell:
    def __init__(self, number = None):
        self.number = number
        self.sides = [Vert.FREE_FLAT, Vert.FREE]*2 #NESW

    def __str__(self) -> str:
        return f"Number:[{self.number}] \nSides: {self.sides}"

    def __repr__(self) -> str:
        return str(self.number)

    def get_number(self):
        return self.number

    def set_side(self, side: Side, state: Vert):
        if side.value%2 == 0:
            self.sides[side.value] = Vert[f"{state.name}_FLAT"]
        else:
            self.sides[side.value] = state

    def set_inv_side(self, side: Side, state: Vert):
        s = Side((side.value+2)%4)
        self.set_side(s, state)

    def get_side(self, side: Side):
        return self.sides[side.value]



class Board:
    # Only can track square fields 


    def __init__(self, size):
        self.size = size
        self.cells : List[Cell] = []

    def str_board(self):
        board = []
        for i in range(0, len(self.cells), self.size):
            row = self.cells[i:i+self.size]
            if i == 0:
                board.append(" "+" ".join([x.get_side(Side.north).value for x in row]))

            bars = [x.get_side(Side.west).value for x in row]
            bars.append(row[-1].get_side(Side.east).value)
            
            fields = [f"{str(x.get_number()):>5}" for x in row]


            line = "".join([x+y  for x, y in zip_l(bars, fields, fillvalue="")])
            board.append(line)
            board.append(" "+" ".join([x.get_side(Side.south).value for x in row]))

        return "\n".join(board)

    def add_cell(self, cell : Cell):
        self.cells.append(cell)

    def __str__(self) -> str:
        return f"Slither board of size: {self.size}\n{self.str_board()}"


