# -*- coding: utf-8 -*-

#Order: Pawn, Knight, Bishop, Rook, Queen, King
black_pieces = ['p', 'n', 'b', 'r', 'q', 'k']
white_pieces = ['P', 'N', 'B', 'R', 'Q', 'K']

#Board, using the representations of the pieces above and spaces for empty squares
starting_state = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
]

#White thenBlack
squares = [' ', '=']

#Inascending order (note: these are used to determine the size of the board, so even
#   if you don't want them to show, fill upthe right amount of indices with spaces)
#   also always make these strings, not ints or whatever else
horizontal_rules = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
vertical_rules = ['1', '2', '3', '4', '5', '6', '7', '8']

#Starting with bottom left corner and moving clockwise
borders = [' ', '|', ' ', '-', ' ', '|', ' ', '-']