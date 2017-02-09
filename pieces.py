# -*- coding: utf-8 -*-

from settings import white_pieces, black_pieces

class Piece:
    text_value = 'X'
    posX = 0
    posY = 0
    team = -1
    blocked_by_pieces = True
    blocked_by_attacks = False

    def __init__(self, posX, posY, team, text):
        self.posX = posX
        self.posY = posY
        self.team = team
        self.text_value = text

    def to_string(self):
        return self.text_value

    def can_move(self, x, y):
        print('Checking if this piece can move like that')
        return False

class King(Piece):

    def __init__(self, posX, posY, team):
        text = 'X'
        if team == 0:
            text = white_pieces[5]
        else:
            text = black_pieces[5]
        Piece.__init__(self, posX, posY, team, text)

        self.blocked_by_attacks = True

    def can_move(self, x, y):
        print('Checking if this piece can move like that')
        return False

class Queen(Piece):

    def __init__(self, posX, posY, team):
        text = 'X'
        if team == 0:
            text = white_pieces[4]
        else:
            text = black_pieces[4]
        Piece.__init__(self, posX, posY, team, text)

    def can_move(self, x, y):
        print('Checking if this piece can move like that')
        return False

class Rook(Piece):

    def __init__(self, posX, posY, team):
        text = 'X'
        if team == 0:
            text = white_pieces[3]
        else:
            text = black_pieces[3]
        Piece.__init__(self, posX, posY, team, text)

    def can_move(self, x, y):
        print('Checking if this piece can move like that')
        return False

class Bishop(Piece):

    def __init__(self, posX, posY, team):
        text = 'X'
        if team == 0:
            text = white_pieces[2]
        else:
            text = black_pieces[2]
        Piece.__init__(self, posX, posY, team, text)

    def can_move(self, x, y):
        print('Checking if this piece can move like that')
        return False

class Knight(Piece):

    def __init__(self, posX, posY, team):
        text = 'X'
        if team == 0:
            text = white_pieces[1]
        else:
            text = black_pieces[1]
        Piece.__init__(self, posX, posY, team, text)

        self.blocked_by_pieces = False

    def can_move(self, x, y):
        print('Checking if this piece can move like that')
        return False

class Pawn(Piece):

    def __init__(self, posX, posY, team):
        text = 'X'
        if team == 0:
            text = white_pieces[0]
        else:
            text = black_pieces[0]
        Piece.__init__(self, posX, posY, team, text)

    def can_move(self, x, y):
        print('Checking if this piece can move like that')
        return False
