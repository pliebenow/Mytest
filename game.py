class Game():
    length = 3
    width = 3

    def __init__(self):
        self.board = [[None] * Game.length for _ in range(Game.width)]

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

    def play(self, player_A, player_B):
        self.draw_board()
        while True:
            self.turn(player_A)
            result = self.evaluate(player_A)
            if result:
                return result
            self.turn(player_B)
            result = self.evaluate(player_B)
            if result:
                return result

    def evaluate(self, player):
        is_full = 0
        for row in range(Game.length):
            counter = 0
            for column in range(Game.width):
                if self.board[row][column] == player.symbol:
                    counter += 1
                if self.board[row][column]:
                    is_full += 1

            if counter == 3:
                return f"{player.player_name} won"

        for column in range(Game.length):
            counter = 0
            for row in range(Game.width):
                if self.board[row][column] == player.symbol:
                    counter += 1

            if counter == 3:
                return f"{player.player_name} won"

        major_counter = 0  # this one: \
        minor_counter = 0  # this one: /

        for row_col in range(Game.length):
            if self.board[row_col][row_col] == player.symbol:
                major_counter += 1
            if self.board[2 - row_col][row_col] == player.symbol:
                minor_counter += 1
            pass
        if major_counter == 3 or minor_counter == 3:
            return f"{player.player_name} won"

        if is_full == Game.width * Game.length:
            return "draw"

        return None


if __name__ == "__main__":
    from player import Player

    battlefield = Game()

    anita = Player(battlefield, "x", "Anita")
    kevin = Player(battlefield, "o", "Kevin")
    final_result = battlefield.play(anita, kevin)
