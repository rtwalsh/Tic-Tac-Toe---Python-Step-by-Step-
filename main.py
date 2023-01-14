import random
import time

WHO_SHOULD_GO_FIRST = "Who should go first? "
COMPUTER = "X"
PLAYER = "O"
CAT = "CAT"
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

def check_for_winner(the_board):
  winning_combinations = [
    [1, 2, 3],
    [1, 5, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [3, 5, 7],
    [4, 5, 6],
    [7, 8, 9]
  ]

  for combination in winning_combinations:
    first_symbol = the_board[combination[0] - 1]
    if first_symbol != EMPTY:
      second_symbol = the_board[combination[1] - 1]
      third_symbol = the_board[combination[2] - 1]
      if first_symbol == second_symbol and first_symbol == third_symbol:
        return first_symbol

  if the_board.count(EMPTY) == 0:
    return CAT
    
  return NONE

def play():
  random.seed()
  whose_turn = greet_player()
  draw_board(board)
  
  winner = NONE
  while winner == NONE:
    if whose_turn == PLAYER:
      player_choice = get_player_choice(board)
      board[player_choice - 1] = PLAYER
      whose_turn = COMPUTER
    else:
      computer_choice = get_computer_choice(board)
      board[computer_choice - 1] = COMPUTER
      whose_turn = PLAYER
    draw_board(board)
    winner = check_for_winner(board)
  
  if winner == PLAYER:
    print("Congratulations!  You won!")
  elif winner == COMPUTER:
    print("Ha!  I won")
  else:
    print("Ah, cat got that game!  We tied.")

play()