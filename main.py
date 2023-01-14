import random
import time

WHO_SHOULD_GO_FIRST = "Who should go first? "
COMPUTER = "X"
PLAYER = "O"
EMPTY = "empty"
NONE = "none"
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

def get_player_choice(the_board):
  print("Your turn.")
  valid_choice = False
  while not valid_choice:
    choice = input("Pick a square by typing its number: ")
    if not choice.isdigit():
      print("Your selection must be a number between 1 and 9.")
    else:
      choice = int(choice)
      if choice < 1 or choice > 9:
        print("Please pick a number between 1 and 9.")
      elif the_board[choice - 1] != EMPTY:
        print("That square has already been taken.")
      else:
        valid_choice = True
  return choice

def get_computer_choice(the_board):
  print("My turn.")
  time.sleep(random.randint(25, 75)/100.0)
  choice = random.randint(1, 9)
  while the_board[choice - 1] != EMPTY:
    time.sleep(random.randint(1, 5)/10.0)
    choice = random.randint(1, 9)
    
  return choice
  
random.seed()
whose_turn = greet_player()
draw_board(board)

winner = NONE
while winner == NONE:
  if whose_turn == PLAYER:
    player_choice = get_player_choice(board)
    board[player_choice - 1] = PLAYER
  else:
    computer_choice = get_computer_choice(board)
    board[computer_choice - 1] = COMPUTER
  draw_board(board)