class Player():

    def __init__(self, battlefield, symbol, player_name):
        self.battlefield = battlefield
        self.symbol = symbol
        # self.turn_tuples = []
        self.player_name = player_name

    def play(self):
        # print(f"its {player}s turn")
        print("\n Where do you want to put your cross?")
        cross_pos_row = input('Row: ')
        cross_pos_column = input('column: ')

        try:
            cross_pos_row = int(cross_pos_row)
            cross_pos_column = int(cross_pos_column)
            # cross_pos_tuple = (cross_pos_row, cross_pos_column)
        except ValueError:
            print("Input was not an integer.")

        # if self.battlefield[cross_pos_row][cross_pos_column]:
        #     print("This Position is already taken")

        # else:
        #     return cross_pos_tuple
        self.battlefield.board[cross_pos_row][cross_pos_column] = self.symbol
        # self.turn_tuples.append(cross_pos_tuple)



