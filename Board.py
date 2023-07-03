
class my_class(object):
    
    board = [["empty" for letter in range(8)] for number in range(8)]





    def __init__(self, NewBoard = True):
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
                    self.board[letter][number] = "empty"

            for number in range(8):
                self.board[1][number] = "pawn"
                self.board[6][number] = "pawn"








