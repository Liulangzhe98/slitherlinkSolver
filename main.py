from board import Board, Cell, Vert, Side
from slitherParser import parser


def get_nbs(index, size):
    rows = []
    if index >= size: # Not on the first row
        rows.append(f'-{size}')
    rows.append("-0")
    if index < (size*size-size): # Not on the last row
        rows.append(f'+{size}')
    cols = []
    if index%size >= 1: # Not on the first col
        cols.append('-1')
    cols.append("-0")
    if index%size < size-1: # Not on the last col
        cols.append("+1")
    
   
    nbs = [index+eval(r)+eval(c) for r in rows for c in cols]
    nbs.remove(index)
    return nbs

def get_plus(index, size):
    plus = []
    if index >= size:
        plus.append(index-size)
    if index%size < size-1:
        plus.append(index+1)
    if index < (size*size-size):
        plus.append(index+size)
    if index%size >= 1:
        plus.append(index-1)
    return plus

PLUS_ALGO = ["-SIZE", "+1", "+SIZE", "-1"]





def solver(board: Board):
    SIZE = board.size
    # Remove all connections next to a 0
   
    for e,c in enumerate(board.cells):
        plus= get_plus(e, SIZE)

        if c.get_number() == 0:
            for x, y in zip(PLUS_ALGO, Side):
                c.set_side(y, Vert.NOT)
                nb = e+eval(x)
                print(f"[{e}. {y:10}] => {nb:>3}")
                if nb in plus:
                    board.cells[nb].set_inv_side(y, Vert.NOT)


    print(board)
    # Game loop should start here
    for _ in range(1):
        for e,c in enumerate(board.cells):
            if c.get_number() == 0:
                continue

            nbs = get_nbs(e, SIZE)
            plus= get_plus(e, SIZE)

            if c.get_number() == 3:
                # Check if one side is blocked -> Take all others
                if Vert.NOT in c.sides or Vert.NOT_FLAT in c.sides:
                    print("Lucky day, we can enter all other lines", plus)
                    for x, y in zip(PLUS_ALGO, Side):
                        if c.get_side(y) == Vert.NOT or c.get_side(y) == Vert.NOT_FLAT:
                            continue
                        c.set_side(y, Vert.TAKEN)
                        nb = e+eval(x)
                        print(f"[{e}. {y:10}] => {nb:>3}")
                        if nb in plus:
                            board.cells[nb].set_inv_side(y, Vert.TAKEN)





    print(board)


    pass

def main():
    print(" == Welcome to the slitherlink solver ==")
    board = parser("input2.txt")
    solver(board)


if __name__ == "__main__":
    main()