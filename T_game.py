
import numpy as np

from T_player import T_player

class T_game():
    
    board_state_A = []
    board_state_B = []
    length = 3
    width = 3
    
    def __init__(self):
       pass 

    def draw_field(player_A,player_B):
        length = T_game.length
        width = T_game.width
        board = np.chararray((3, 3))
        for row in range(length):
                for column in range(width):
                    print("|",end="")
                    print("__",end="")
                    #if row == int(cross_x) and column == int(cross_y):
                    #    print("x",end="")
                    for tuple in T_game.board_state_A:
                        if row == int(tuple[0]) and column == int(tuple[1]):
                            print(player_A.symbol,end="")
                            board[row][column]= player_A.symbol
                    for tuple in T_game.board_state_B:
                        if row == int(tuple[0]) and column == int(tuple[1]):
                            print(player_B.symbol,end="")
                            board[row][column]= player_B.symbol
                print("\n")
        return board


    def play(self,player_A,player_B):
        board = T_game.draw_field(player_A,player_B) 
        while True :
            board = [[]]
            if player_A.turn == True:
                T_game.board_state_A.append(T_player.play(player_A))
                board = T_game.draw_field(player_A,player_B) 
                player_A.turn = False
                player_B.turn = True
            else:
                T_game.board_state_B.append(T_player.play(player_B))
                board = T_game.draw_field(player_A,player_B) 
                player_B.turn =  False
                player_A.turn = True
            print(T_game.evaluate(player_A,board))
            print(T_game.evaluate(player_B,board))
            if (T_game.evaluate(player_A,board) and T_game.evaluate(player_B,board)):
                print("GAME OVER") 
                break

    def evaluate(player,board):
            is_full = 0
            counter = 0
            print(T_game.board_state_A)
            print(T_game.board_state_B)
            for row in range(3):
                for column in range(3):
                    #print(board[row][column])
                    if board[row][column] == player.symbol:
                        counter += 1
                    else:
                        continue

                if counter == 3:
                    #print(f"{player} wins")
                    #self.print_board()
                    return True

            if is_full == 9:
                print("draw")
                return True
            return False 
