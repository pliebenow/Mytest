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
                # print(f"row {row}, col: {column}")
                # print(Game.board[row][column])
                if Game.board[row][column] == player.symbol:
                    counter += 1
                if Game.board[row][column]:
                    is_full += 1

            if counter == 3:
                # print(f"{player} wins")
                # self.print_board()
                return f"{player.player_name} won"

        counter1 = 0
        counter2 = 0

        for row_col in range(Game.length):
            if Game.board[row_col][row_col] == player.symbol:
                counter1 += 1
            if Game.board[1 - row_col][1 - row_col] == player.symbol:
                counter2 += 1
        # print(f"counters: {counter1}, {counter2}")
        if counter1 == 3 or counter2 == 3:
            return f"{player.player_name} won"

        if is_full == Game.width * Game.length:
            return "draw"

        return None


