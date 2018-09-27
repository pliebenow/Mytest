class T_player():

    def __init__(self,game,symbol,turn):
        self.game = game
        self.symbol = symbol
        self.turn = turn

    def play(self):
        # print(f"its {player}s turn")
        print("\n Where do you want to put your cross?")
        cross_pos_row = input('Row: ')
        cross_pos_column = input('column: ')

        try:
            cross_pos_row = int(cross_pos_row)
            cross_pos_column = int(cross_pos_column)
            cross_pos_tuple = (cross_pos_row, cross_pos_column)
        except ValueError:
            print("Input was not an integer.")
        
        return cross_pos_tuple


