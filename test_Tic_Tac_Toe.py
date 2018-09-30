from game import Game
from player import Player
import types


def mockup_factory(draws):
    def play_mockup(self):
        coordinates = draws.pop()
        self.battlefield.board[coordinates[0]][coordinates[1]] = self.symbol
        # self.turn_tuples.append(coordinates)
    return play_mockup


battlefield = Game(print_board=False)
draws_player1 = [(2, 1), (1, 2), (2, 2), (1, 1), (0, 0)]
draws_player2 = [(2, 0), (1, 0), (0, 2), (0, 1)]

Felix = Player(battlefield, "o", "Felix")
Felix.play = types.MethodType(mockup_factory(draws_player1), Felix)
Paul = Player(battlefield, "*", "Paul")
Paul.play = types.MethodType(mockup_factory(draws_player2), Paul)

final_result = battlefield.play(Felix, Paul)
assert final_result == "Felix won", "Test game 1 does not bear the right " + \
        f"result. It says '{final_result}' instead of 'Felix won'"


# second game

battlefield = Game(print_board=False)
# battlefield = Game()
draws_player1 = [(2, 0), (2, 1), (1, 2), (2, 2), (0, 0)]
draws_player2 = [(1, 0), (1, 1), (0, 1), (0, 2)]

anita = Player(battlefield, "x", "Anita")
anita.play = types.MethodType(mockup_factory(draws_player1), anita)

kevin = Player(battlefield, "o", "Kevin")
kevin.play = types.MethodType(mockup_factory(draws_player2), kevin)

final_result = battlefield.play(anita, kevin)

assert final_result == "Anita won", "Test game 2 does not bear the right " + \
    f"result, it says '{final_result}' instead of 'Anita won'"


# third game

battlefield = Game(print_board=False)
draws_player1 = [(2, 2), (0, 1), (0, 2), (1, 1), (2, 0)]
draws_player2 = [(2, 1), (1, 2), (1, 0), (0, 0)]

theobald = Player(battlefield, "x", "Theobald")
theobald.play = types.MethodType(mockup_factory(draws_player1), theobald)

mara = Player(battlefield, "o", "Mara")
mara.play = types.MethodType(mockup_factory(draws_player2), mara)

final_result = battlefield.play(theobald, mara)

assert final_result == "Theobald won", "Test game 3 does not bear the right " + \
    f"result, it says '{final_result}' instead of 'Theobald won'"

# # fourth game

battlefield = Game(print_board=False)
draws_player1 = [(0, 0), (2, 2), (1, 0), (0, 2), (2, 1)]
draws_player2 = [(1, 1), (1, 2), (2, 0), (0, 1)]

theobald = Player(battlefield, "x", "Theobald")
theobald.play = types.MethodType(mockup_factory(draws_player1), theobald)

mara = Player(battlefield, "o", "Mara")
mara.play = types.MethodType(mockup_factory(draws_player2), mara)

final_result = battlefield.play(theobald, mara)

assert final_result == "draw", "Test game 4 does not bear the right " + \
    f"result, it says '{final_result}' instead of 'Theobald won'"

