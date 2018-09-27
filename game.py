class Game():
    length = 3
    width = 3
    board = [[None] * 3 for _ in range(3)]

    def __init__(self):
        pass

    def draw_board(self):
        for row in self.board:
            print("|", end="")
            for entry in row:
                if entry:
                    print(" " + entry + " ", end="")
                else:
                    print("   ", end="")
                print("|", end="")
            print('\n')
            # for _ in row:
            #     print("__", end="")
        print("\n\n")

    def turn(self, player):
        player.play()
        self.draw_board()
        self.evaluate(player)

    def play(self, player_A, player_B):
        self.draw_board()
        while True:
            self.turn(player_A)
            self.turn(player_B)
            if (self.evaluate(player_A) and self.evaluate(player_B)):
                print("GAME OVER")
                break

    def evaluate(self, player):
            is_full = 0
            counter = 0
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
