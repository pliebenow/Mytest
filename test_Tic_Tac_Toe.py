from T_game import T_game
from T_player import T_player

battlefield = T_game()

Felix = T_player(battlefield,"o",True)
Paul = T_player(battlefield,"*",False)

T_game.play(battlefield,Felix,Paul)
