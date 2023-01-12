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

print("Let's play Tic Tac Toe.  I'll be X, and you can be O.")
whoseTurn = input("Who should go first? ").upper()
while whoseTurn != "X" and whoseTurn != "O":
  print("Please type X or O.")
  whoseTurn = input("Who should go first? ")
  
draw_board(board)