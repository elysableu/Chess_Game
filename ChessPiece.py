
'''
class ChessPiece


used as a template for all chess pieces available in the game

constructor: (name, color, xpos, ypos)
    no args- makes a white pawn at position a0

    name - name of the piece. should be pawn, knight, bishop, rook, queen, or king
    color - what color the piece is. should be black or white
    xpos - the letter position of the piece. should be a, b, c, d, e, f, g, or h
    ypos - the number position of the piece. should be 1, 2, 3, 4, 5, 6, 7, or 8


'''
class ChessPiece:

    #holds the name of the piece. pawn, knight, bishop, rook, queen, king
    __piece_type = ""

    #which color this piece is. either black or white
    __piece_color = ""

    #tracks position on board. letter == A-H, number == 1-8
    __letter_position = 'a'
    __number_position = 0


    def __init__(self, name="pawn", color="white", xpos='a', ypos=0):
        __piece_type = name
        __piece_color = color
        __letter_position = xpos
        __number_position = ypos
        
    

    #get functions

    def get_piece_type(self):
        return self.__piece_type

    def get_color(self):
        return self.__piece_color

    def get_position(self):
        position = (self.__letter_position, self.__number_position)
        return position


    #set functions

    def set_piece_type(self, newType):
        self.__piece_type = newType

    def set_piece_color(self, newcolor):
        self.set_piece_color = newcolor

    def set_position(self, xpos, ypos):
        self.__letter_position = xpos
        self.__number_position = ypos











    




