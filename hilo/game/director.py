from game.dealer import Dealer

class Director():

    def __init__(self):

        self.keep_playing = True
        self.score = 300
        self.dealer = Dealer()

    def start_game(self):

        while self.keep_playing:
            self.get_card()
            self.total_score()
            self.do_output()
            

    # I've changed this name from get_input to get_card
    # bacause we are going to get the card N° from the dealer
    def get_card(self):

        self.dealer.deal_card()

    # I'm not sure if we should use this function now... 
    def total_score(self):
        pass
        

    def do_output(self):

        print(f'The card is {self.dealer.previous_card}')
        # not sure if this input should be here, or in another place.
        user_input = input('Higher or lower? [h/l] ')
        # Also we should get the input of the user and pass that value to the compare_card,
        # that comes from the dealer.
        self.score += self.dealer.compare_card(user_input)

        print(f'Next card was: {self.dealer.previous_card}')

        print(f'Your score is {self.score}')

        playing = input('Keep playing? [y/n] ')

        # It may be possible it's necessary to adjust this. 
        # Maybe the dealer should handle if they can keep playing
        # since the score may be 0 and they could not be able to play anymore.
        if playing.lower() == 'y':
            self.start_game()
        else:
            print('Good bye baby!')


# I didn't add any comment to the functions, that might be necessary