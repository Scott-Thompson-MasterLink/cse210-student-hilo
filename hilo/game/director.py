from game.dealer import Dealer

class Director():

    def __init__(self, score):

        self.keep_playing = True
        self.score = 300
        self.dealer = Dealer()

    def start_game(self):
        pass

    def total_score(self):
        pass
