WHO_SHOULD_GO_FIRST = "Who should go first? "
COMPUTER = "X"
PLAYER = "O"
EMPTY = "empty"
board = [ 
  EMPTY, EMPTY, EMPTY,
  EMPTY, EMPTY, EMPTY,
  EMPTY, EMPTY, EMPTY
]

def get_symbol(the_board, square_number):
  symbol = board[square_number - 1]
  if symbol == EMPTY:
    return square_number

  return symbol
  
def draw_board(the_board):
  for row in range(3):
    print("   |   |   ")
    print(" {} | {} | {} ".format(get_symbol(the_board, row * 3 + 1), get_symbol(the_board, row * 3 + 2), get_symbol(board, row * 3 + 3)))
    print("   |   |   ")
    if row != 2:
      print("---+---+---")

def greet_player():
  print("Let's play Tic Tac Toe.  I'll be {}, and you can be {}.".format(COMPUTER, PLAYER))
  choice = input(WHO_SHOULD_GO_FIRST).upper()
  while choice != COMPUTER and choice != PLAYER:
    print("Please type {} or {}.".format(COMPUTER, PLAYER))
    choice = input(WHO_SHOULD_GO_FIRST).upper()
  return choice
  
whoseTurn = greet_player()
draw_board(board)