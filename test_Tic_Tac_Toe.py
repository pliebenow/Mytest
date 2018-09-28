from game import Game
from player import Player


def mockup_factory(draws):
    def play_mockup(self):
        coordinates = draws.pop()
        self.battlefield.board[coordinates[0]][coordinates[1]] = self.symbol
        # self.turn_tuples.append(coordinates)
    return play_mockup


battlefield = Game()
draws = [(0, 0), (0, 1), (1, 1), (0, 2), (2, 2), (1, 0), (1, 2), (2, 0), (2, 1)]
Player.play = mockup_factory(draws)

Felix = Player(battlefield, "o", "Felix")
Paul = Player(battlefield, "*", "Paul")

final_result = battlefield.play(Felix, Paul)
assert final_result == "Felix won", "Test game 1 does not bear the right " + \
        f"result. It says '{final_result}' instead of 'Felix won'"


# second game

battlefield = Game()
# draws_player1 = [(0, 0)]
# draws_player2 = [(0, 2)]
draws = [(0, 0), (0, 2), (2, 2), (0, 1), (1, 2), (1, 1), (2, 1), (1, 0), (2, 0)]
Player.play = mockup_factory(draws)

anita = Player(battlefield, "x", "Anita")
# anita.play = mockup_factory(draws_player1)
kevin = Player(battlefield, "o", "Kevin")
# kevin.play = mockup_factory(draws_player2)
final_result = battlefield.play(anita, kevin)

assert final_result == "Anita won", "Test game 2 does not bear the right " + \
    f"result, it says '{final_result}' instead of 'Anita won'"


# third game

battlefield = Game()
draws = [(2, 0), (0, 0), (1, 1), (1, 0), (0, 2), (1, 2), (0, 1), (2, 1), (2, 2)]
Player.play = mockup_factory(draws)

theobald = Player(battlefield, "x", "Theobald")
mara = Player(battlefield, "o", "Mara")
final_result = battlefield.play(theobald, mara)

assert final_result == "Theobald won", "Test game 3 does not bear the right " + \
    f"result, it says '{final_result}' instead of 'Theobald won'"

# fourth game

battlefield = Game()
draws = [(2, 1), (0, 1), (0, 2), (2, 0), (1, 0), (1, 2), (2, 2), (1, 1), (0, 0)]
Player.play = mockup_factory(draws)

theobald = Player(battlefield, "x", "Theobald")
mara = Player(battlefield, "o", "Mara")
final_result = battlefield.play(theobald, mara)

assert final_result == "draw", "Test game 4 does not bear the right " + \
    f"result, it says '{final_result}' instead of 'Theobald won'"

