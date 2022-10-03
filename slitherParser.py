from matplotlib.pyplot import text
from board import *



#TODO: Check if input is correct size
def parser(file_path: str) -> Board:
    text_board = [x.strip() for x in open(file_path, "r").readlines()]
    size = len(text_board)
    if any (size != len(i) for i in text_board):
        raise ValueError(f"{text_board} is not of correct size ({size})")

    slither_board = Board(size)
    for row in text_board:
        for cell in row:
            new_cell = Cell((int(cell) if cell.isdigit() else None))

            slither_board.add_cell(new_cell)
    return slither_board
    