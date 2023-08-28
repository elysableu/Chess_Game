
from typing import Self


class my_class(object):
    
    _board = [["empty" for letter in range(8)] for number in range(8)]





    def __init__(self, NewBoard = True):
        #set up a new board with all pieces in their starting location
        if NewBoard:
            """
            pawn:   (1,0-7) (6, 0-7)
            rook:   0,0 - 0,7 - 7,0 - 7,7
            bishop: 0,1 - 0,6 - 7,1 - 7,6
            knight: 0,2 - 0,5 - 7,2 - 7,5
            queen:  0,3 - 7,3
            king:   0,4 - 7-4
            """

            for letter in range(8):
                for number in range(8):
                    self._board[letter][number] = "empty"

            for number in range(8):
                self._board[1][number] = "pawn"
                self._board[6][number] = "pawn"

            self._board[0][0] = self._board[0][7] = self._board[7][0] = self._board[7][7] = "rook"
            self._board[0][1] = self._board[0][6] = self._board[7][1] = self._board[7][6] = "bishop"
            self._board[0][2] = self._board[0][5] = self._board[7][2] = self._board[7][5] = "knight"
            self._board[0][3] = self._board[7][3] = "queen"
            self._board[0][4] = self._board[7][4] = "king"

        #what to do if this is not for a new game
        #possibly implement a way to set up board based on a previous boardstate
        #NOT CURRENTLY IMPLEMENTED
        if not NewBoard:
            pass



    def getBoardState():
        pass

    def movePiece():
        #code to move a piece
        pass



