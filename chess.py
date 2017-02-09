# -*- coding: utf-8 -*-

#Chess program
#Kyle Engelken

from settings import *
from board import *

def main():
    game_board = Board()
    play_game(game_board)

def read_indices(input):
    if input[2] == ' ':
        first = input[0]
        second = input[1]
        third = input[3]
        fourth = input[4]

        if first in horizontal_rules and third in horizontal_rules:
            first = horizontal_rules.index(first)
            third = horizontal_rules.index(third)

            if second in vertical_rules and fourth in vertical_rules:
                second = vertical_rules.index(second)
                fourth = vertical_rules.index(fourth)

                return ((first, second), (third, fourth))
    return ((-1, -1), (-1, -1))

def play_game(game_board):
    turn = 0
    game_board.print_board()
    move = input('Please make a move >> ')
    while move != 'quit':
        failure = False
        if len(move) == 5:
            move = read_indices(move)
            if move[0][0] == -1:
                failure = True
            else:
                check = check_move(move)
                if check:
                    make_move(move)
                else:
                    failure = True
        else:
            failure = True

        if failure:
            print
            print('Invalid move!')
            print('Moves must be made in the format of the space you wish to move from then the space you wish to move to.')
            print('i.e. A2 A3')
        print
        game_board.print_board()
        move = raw_input('Please make a move >> ')

def check_move(move):
    x1 = move[0][0]
    y1 = move[0][1]
    x2 = move[1][0]
    y2 = move[1][1]

    p = spaces[x1][y1]
    check = p.can_move(x2, y2)

    print('Checking if the piece is effected by collissions in the first place')
    print('If so, checking if there are collisions')
    print('If there is a collision, checking the teams of both pieces to see if it is a capture')
    print('Checking if the move would result in a check for the other King')
    print('Checking if the piece is a King and if so checking for checks')
    print('If the piece is not a King, checking to see if the King is in check')
    print('If so, checking to see if this move would make the King not in check')
    print('Check for checkmate')
    print('Check for  stalemate')

#Boilerplate to call main()
if __name__ == '__main__':
  main()