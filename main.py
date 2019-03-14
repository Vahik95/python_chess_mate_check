from Board import *

# Please give the inputs in the syntax which is given below(using the names king,queen,bishop,horse)
# You can also print the board, but be careful as there are 2 kings but the color
# is not mentioned in my printing, so it may confuse you))


brd = Board()
brd.add_piece('king', 'black', 'a1')
brd.add_piece('king', 'white', 'h2')
brd.add_piece('queen', 'white', 'd2')
brd.add_piece('bishop', 'white', 'd8')
brd.add_piece('horse', 'white', 'c2')

# brd.print_board()

brd.check_the_game()
