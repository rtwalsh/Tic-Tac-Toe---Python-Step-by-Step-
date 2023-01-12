EMPTY = "empty"
board = [ 
  EMPTY, EMPTY, EMPTY,
  EMPTY, EMPTY, EMPTY,
  EMPTY, EMPTY, EMPTY
]

def get_symbol(the_board, square_number):
  symbol = board[square_number - 1]
  if (symbol == EMPTY):
    return square_number

  return symbol
  
def draw_board(the_board):
  print("   |   |   ")
  print(" {} | {} | {} ".format(get_symbol(the_board, 1), get_symbol(the_board, 2), get_symbol(board, 3)))
  print("   |   |   ")
  print("---+---+---")
  print("   |   |   ")
  print(" {} | {} | {} ".format(get_symbol(the_board, 4), get_symbol(the_board, 5), get_symbol(the_board, 6)))
  print("   |   |   ")
  print("---+---+---")
  print("   |   |   ")
  print(" {} | {} | {} ".format(get_symbol(the_board, 7), get_symbol(the_board, 8), get_symbol(the_board, 9)))
  print("   |   |   ")

draw_board(board)