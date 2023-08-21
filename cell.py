import random
class Player:
  def __init__(self, selected_piece):
     self.selected_piece = selected_piece    # to choose X or O

class Board:
  def __init__(self):
        self.board = []
        self.num = 1
        for i in range(4):
            self.board_row = []
            for j in range(4):
                self.board_row.append(self.num)
                self.num += 1
            self.board.append(self.board_row)


  def print(self):
     for row in range(4):
       for col in range(4):
         if (len(str(self.board[row][col]))==1) :
           print(f"| {self.board[row][col]} |",end="")
         else:
             print(f"|{self.board[row][col]} |", end="")
       print()
     print()

  def add_piece(self, number, player_piece):
      for row in range(4):
          for col in range(4):
              if self.board[row][col] == number:
                  self.board[row][col] = player_piece
                  return True
      print("Invalid move")  # when the user puts a wrong number
      return False

  def reset(self):
      self.board = []
      self.num = 1
      for i in range(4):
          self.board_row = []
          for j in range(4):
              self.board_row.append(self.num)
              self.num += 1
          self.board.append(self.board_row)

  def is_board_full(self):
        for row in self.board:
            for cell in row:
                if isinstance(cell, int):  # Check if the cell is still an integer (not occupied by a player piece)
                    return False
        return True


  def checkWin(self, piece):
      # Check diagonal locations for win
      self.count = 0
      self.ccount = 0
      for row in range(4):
          for col in range(4):
              if self.board[row][col] == piece and row == col:
                  self.count += 1
              if self.board[row][col] == piece and row + col == 3:
                  self.ccount += 1
      if self.count == 4 or self.ccount == 4:
          return True

      # Check horizontal locations for win
      for row in range(4):
          for col in range(1):
              if (
                      self.board[row][col] == piece
                      and self.board[row][col + 1] == piece
                      and self.board[row][col + 2] == piece
                      and self.board[row][col + 3] == piece
              ):
                  print(f"Player {piece} wins")
                  return True
      # Check vertical locations for win
      for row in range(1):
          for col in range(4):
              if (
                      self.board[row][col] == piece
                      and self.board[row + 1][col] == piece
                      and self.board[row + 2][col] == piece
                      and self.board[row + 3][col] == piece
              ):
                  print(f"Player {piece} wins")
                  return True
      return False

class Game:
    def __init__(self):
        self.board = Board()
        self.player1 = None
        self.player2 = None
        self.current_player = None

    def setup_players(self):
        piece1 = input("Enter player 1's symbol (X/O): ").upper()
        self.player1 = Player(piece1)

        piece2 = 'X' if piece1 == 'O' else 'O'
        self.player2 = Player(piece2)
        self.current_player = self.player1

    def switch_player(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    def get_computer_move(self):
        available_cells = [cell for row in self.board.board for cell in row if isinstance(cell, int)]
        return random.choice(available_cells)

    def play(self):
        x = input("Do you want to play vs another player or computer? (p/c): ").lower()

        if x == "p":
            self.setup_players()
            while True:
                self.board.print()
                print(f"It's {self.current_player.selected_piece}'s turn.")
                cell_num = int(input("Enter the cell number (1-16): "))
                if cell_num < 1 or cell_num > 16:
                    print("Invalid cell number. Please enter a number between 1 and 16.")
                    continue

                if self.board.add_piece(cell_num, self.current_player.selected_piece):
                    self.board.print()
                    if self.board.checkWin(self.current_player.selected_piece):
                        print(f"{self.current_player.selected_piece} wins!")
                        break
                    elif self.board.is_board_full():  # Check for a draw
                        print("It's a draw!")
                        self.board.reset()
                        game = Game()
                        game.play()
                    else:
                        self.switch_player()
                else:
                    print("Invalid move. The cell is already occupied.")
        else:
            self.setup_players()
            while True:
                self.board.print()
                print(f"It's {self.current_player.selected_piece}'s turn.")

                if self.current_player == self.player1:
                    cell_num = int(input("Enter the cell number (1-16): "))
                    if cell_num < 1 or cell_num > 16:
                        print("Invalid cell number. Please enter a number between 1 and 16.")
                        continue
                else:
                    cell_num = self.get_computer_move()

                if self.board.add_piece(cell_num, self.current_player.selected_piece):
                    self.board.print()
                    if self.board.checkWin(self.current_player.selected_piece):
                        print(f"{self.current_player.selected_piece} wins!")
                        break
                    elif self.board.is_board_full():
                        print("It's a draw!")
                        self.board.reset()
                        game = Game()
                        game.play()
                    else:
                        self.switch_player()
                else:
                    print("Invalid move. The cell is already occupied.")



# # |  O  |     |    | X  |
# # |     | O   | X  |    |
# # |     | X   | O  |    |
# # | X   | X   | X  | O  |

game=Game()
game.play()
