from game import Game
from player import Player

battlefield = Game()

draws = [(i, j) for i in range(3) for j in range(3)]


def play_mockup(self):
    coordinates = draws.pop()
    self.battlefield.board[coordinates[0]][coordinates[1]] = self.symbol
    self.turn_tuples.append(coordinates)


Player.play = play_mockup

Felix = Player(battlefield, "o", True)
Paul = Player(battlefield, "*", False)


# if you want to give Felix and Paul specific instructions.
# As is they both get the same instruction, the method play_mockup
# Felix.play = play_mockup
# Paul.play = play_mockup

battlefield.play(Felix, Paul)
