
import numpy as np

from player import Player


class Game():
    length = 3
    width = 3
    board = [[None] * 3 for _ in range(3)]

    def __init__(self):
        self.board_state_A = []
        self.board_state_B = []

    def draw_field(self, player_A, player_B):
        board = np.chararray((Game.length, Game.width))
        for row in range(Game.length):
                for column in range(Game.width):
                    print("|", end="")
                    print("__", end="")
                    # if row == int(cross_x) and column == int(cross_y):
                    #    print("x",end="")
                    for tuple in self.board_state_A:
                        if row == int(tuple[0]) and column == int(tuple[1]):
                            print(player_A.symbol, end="")
                            board[row][column] = player_A.symbol
                    for tuple in self.board_state_B:
                        if row == int(tuple[0]) and column == int(tuple[1]):
                            print(player_B.symbol, end="")
                            board[row][column] = player_B.symbol
                print("\n")
        return board

    def play(self, player_A, player_B):
        self.draw_field(player_A, player_B)
        while True:
            if player_A.turn:
                self.board_state_A.append(Player.play(player_A))
                self.draw_field(player_A, player_B)
                player_A.turn = False
                player_B.turn = True
            else:
                self.board_state_B.append(Player.play(player_B))
                self.draw_field(player_A, player_B)
                player_B.turn = False
                player_A.turn = True
            print(self.evaluate(player_A))
            print(self.evaluate(player_B))
            if (self.evaluate(player_A) and self.evaluate(player_B)):
                print("GAME OVER")
                break

    def evaluate(self, player):
            is_full = 0
            counter = 0
            print(self.board_state_A)
            print(self.board_state_B)
            for row in range(Game.length):
                for column in range(Game.width):
                    # print(f"row {row}, col: {column}")
                    # print(Game.board[row][column])
                    if Game.board[row][column] == player.symbol:
                        counter += 1
                    else:
                        continue

                if counter == 3:
                    # print(f"{player} wins")
                    # self.print_board()
                    return True

            if is_full == 9:
                print("draw")
                return True
            return False
