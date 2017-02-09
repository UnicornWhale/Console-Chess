# -*- coding: utf-8 -*-

from settings import *
from pieces import *

class Board:
    spaces = []
    pieces = []

    def __init__(self):
        self.setup_board()
        self.setup_pieces()

    def setup_board(self):
        s1 = squares[0]
        s2 = squares[1]

        even1 = 0
        for y in range(len(vertical_rules)):
            row = []
            even2 = 0

            for x in range(len(horizontal_rules)):
                if even1 == 0:
                    if even2 == 0:
                        row.append(Space(s1))
                        even2 = 1
                    else:
                        row.append(Space(s2))
                        even2 = 0
                else:
                    if even2 == 0:
                        row.append(Space(s2))
                        even2 = 1
                    else:
                        row.append(Space(s1))
                        even2 = 0
            self.spaces.append(row)

            if even1 == 0:
                even1 = 1
            else:
                even1 = 0

    def setup_pieces(self):
        b = black_pieces
        w = white_pieces
        ss = starting_state

        for y in range(len(vertical_rules)):
            for x in range(len(horizontal_rules)):
                if ss[y][x] in w:
                    i = w.index(ss[y][x])
                    if i == 0:
                        p = pawn(x, y, 0)
                        self.pieces.append(p)
                        self.spaces[x][y].set_occupant(p)
                    elif i == 1:
                        p = knight(x, y, 0)
                        self.pieces.append(p)
                        self.spaces[x][y].set_occupant(p)
                    elif i == 2:
                        p = bishop(x, y, 0)
                        self.pieces.append(p)
                        self.spaces[x][y].set_occupant(p)
                    elif i == 3:
                        p = rook(x, y, 0)
                        self.pieces.append(p)
                        self.spaces[x][y].set_occupant(p)
                    elif i == 4:
                        p = queen(x, y, 0)
                        self.pieces.append(p)
                        self.spaces[x][y].set_occupant(p)
                    elif i == 5:
                        p = king(x, y, 0)
                        self.pieces.append(p)
                        self.spaces[x][y].set_occupant(p)
                elif ss[y][x] in b:
                    i = b.index(ss[y][x])
                    if i == 0:
                        p = pawn(x, y, 1)
                        self.pieces.append(p)
                        self.spaces[x][y].set_occupant(p)
                    elif i == 1:
                        p = knight(x, y, 1)
                        self.pieces.append(p)
                        self.spaces[x][y].set_occupant(p)
                    elif i == 2:
                        p = bishop(x, y, 1)
                        self.pieces.append(p)
                        self.spaces[x][y].set_occupant(p)
                    elif i == 3:
                        p = rook(x, y, 1)
                        self.pieces.append(p)
                        self.spaces[x][y].set_occupant(p)
                    elif i == 4:
                        p = queen(x, y, 1)
                        self.pieces.append(p)
                        self.spaces[x][y].set_occupant(p)
                    elif i == 5:
                        p = king(x, y, 1)
                        self.pieces.append(p)
                        self.spaces[x][y].set_occupant(p)

    def print_board(self):
        v = vertical_rules
        h = horizontal_rules
        b = borders

        print(' ' + b[2] + b[3] + b[3] + b[3] + b[3] + b[3] + b[3] + b[3] + b[3] + b[4])
        for y in range(len(v)):
            to_output = v[y] + b[1]
            for x in range(len(h)):
                to_output += (self.spaces[x][y]).to_string()
            to_output += b[5]
            print(to_output)
        print(' ' + b[0] + b[7] + b[7] + b[7] + b[7] + b[7] + b[7] + b[7] + b[7] + b[6])
        print(' ' + ' ' + h[0] + h[1] + h[2] + h[3] + h[4] + h[5] + h[6] + h[7] + ' ')

class Space:
    occupied = False
    occupant = None
    string_value = ' '

    def __init__(self, text):
        self.string_value = text

    def to_string(self):
        if self.occupied:
            return self.occupant.to_string()
        else:
            return self.string_value

    def set_occupant(self, p):
        self.occupied = True
        self.occupant = p

    def clear_occupant(self):
        self.occupied = False
        self.occupant = None