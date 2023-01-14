import random
import time

class Game:
  WHO_SHOULD_GO_FIRST = "Who should go first? "
  COMPUTER = "X"
  PLAYER = "O"
  CAT = "CAT"
  EMPTY = "empty"
  NONE = "none"
  WINNING_COMBINATIONS = [
  [1, 2, 3],
  [1, 5, 9],
  [1, 4, 7],
  [2, 5, 8],
  [3, 6, 9],
  [3, 5, 7],
  [4, 5, 6],
  [7, 8, 9]
]

  def __init__(self):
    self.board = [ 
      Game.EMPTY, Game.EMPTY, Game.EMPTY,
      Game.EMPTY, Game.EMPTY, Game.EMPTY,
      Game.EMPTY, Game.EMPTY, Game.EMPTY
    ]
    self.winner = Game.NONE
    
  def get_symbol(self, square_number):
    symbol = self.board[square_number - 1]
    if symbol == Game.EMPTY:
      return square_number
  
    return symbol
    
  def draw_board(self):
    for row in range(3):
      print("   |   |   ")
      print(" {} | {} | {} ".format(self.get_symbol(row * 3 + 1), self.get_symbol(row * 3 + 2), self.get_symbol(row * 3 + 3)))
      print("   |   |   ")
      if row != 2:
        print("---+---+---")
  
  def greet_player(self):
    print("Let's play Tic Tac Toe.  I'll be {}, and you can be {}.".format(Game.COMPUTER, Game.PLAYER))
    choice = input(Game.WHO_SHOULD_GO_FIRST).upper()
    while choice != Game.COMPUTER and choice != Game.PLAYER:
      print("Please type {} or {}.".format(Game.COMPUTER, Game.PLAYER))
      choice = input(Game.WHO_SHOULD_GO_FIRST).upper()
    return choice
  
  def get_player_choice(self):
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
        elif self.board[choice - 1] != Game.EMPTY:
          print("That square has already been taken.")
        else:
          valid_choice = True
    return choice
  
  def get_computer_choice(self):
    print("My turn.")
    time.sleep(random.randint(25, 75)/100.0)
    choice = random.randint(1, 9)
    while self.board[choice - 1] != Game.EMPTY:
      time.sleep(random.randint(1, 5)/10.0)
      choice = random.randint(1, 9)
      
    return choice
  
  def check_for_winner(self):  
    for combination in Game.WINNING_COMBINATIONS:
      first_symbol = self.board[combination[0] - 1]
      if first_symbol != Game.EMPTY:
        second_symbol = self.board[combination[1] - 1]
        third_symbol = self.board[combination[2] - 1]
        if first_symbol == second_symbol and first_symbol == third_symbol:
          return first_symbol
  
    if self.board.count(Game.EMPTY) == 0:
      return Game.CAT
      
    return Game.NONE

  def report_winner(self):
    if self.winner == Game.PLAYER:
      print("Congratulations!  You won!")
    elif self.winner == Game.COMPUTER:
      print("Ha!  I won")
    else:
      print("Ah, cat got that game!  We tied.")
    
  def play(self):
    random.seed()
    whose_turn = self.greet_player()
    self.draw_board()
    
    while self.winner == Game.NONE:
      if whose_turn == Game.PLAYER:
        player_choice = self.get_player_choice()
        self.board[player_choice - 1] = Game.PLAYER
        whose_turn = Game.COMPUTER
      else:
        computer_choice = self.get_computer_choice()
        self.board[computer_choice - 1] = Game.COMPUTER
        whose_turn = Game.PLAYER
      self.draw_board()
      self.winner = self.check_for_winner()

    self.report_winner()

game = Game()
game.play()