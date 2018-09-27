from game import Game
from player import Player


def mockup_factory(draws):
    def play_mockup(self):
        coordinates = draws.pop()
        self.battlefield.board[coordinates[0]][coordinates[1]] = self.symbol
        # self.turn_tuples.append(coordinates)
    return play_mockup


battlefield = Game()
random_draws = [(i, j) for i in range(3) for j in range(3)]
Player.play = mockup_factory(random_draws)

Felix = Player(battlefield, "o", "Felix")
Paul = Player(battlefield, "*", "Paul")


# if you want to give Felix and Paul specific instructions.
# As is they both get the same instruction, the method play_mockup
# Felix.play = play_mockup
# Paul.play = play_mockup

final_result = battlefield.play(Felix, Paul)
assert (final_result == "Felix won", "Test game one does not bear the right result.")


# second game

# battlefield = Game()
# draws_player1 = [(0, 0)]
# draws_player2 = [(0, 2)]

# anita = Player(battlefield, "x", "Anita")
# anita.play = mockup_factory(draws_player1)
# kevin = Player(battlefield, "o", "Kevin")
# kevin.play = mockup_factory(draws_player2)
# final_result = battlefield.play(anita, kevin)


# print("who won?", final_result)
# print("\n\n")
