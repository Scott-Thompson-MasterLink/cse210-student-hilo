from colorama import  Fore
from colorama import Style
from game.dealer import Dealer

class Director():

    def __init__(self):

        self.keep_playing = True
        self.score = 300
        self.dealer = Dealer()
        self.p_card = ''
        self.n_card = ''


    def start_game(self):

        while self.keep_playing:
            self.get_card()
            self.do_output()
            self.track_score()
            

    # I've changed this name from get_input to get_card
    # bacause we are going to get the card N° from the dealer
    def get_card(self):

        self.dealer.deal_card()

        if self.dealer.previous_card == 13:
            self.p_card = 'King'
        elif self.dealer.previous_card == 12:
            self.p_card = 'Queen'
        elif self.dealer.previous_card == 11:
            self.p_card = 'Jack'
        elif self.dealer.previous_card == 1:
            self.p_card = 'Ace'
        else:
            self.p_card = str(self.dealer.previous_card)


        if self.dealer.new_card == 13:
            self.n_card = 'King'
        elif self.dealer.new_card == 12:
            self.n_card = 'Queen'
        elif self.dealer.new_card == 11:
            self.n_card = 'Jack'
        elif self.dealer.new_card == 1:
            self.n_card = 'Ace'
        else:
            self.n_card = str(self.dealer.new_card)

    # I've changed the name of this function in order to track the score
    # and display if the user lost the game
    def track_score(self):
        
        if self.score <= 0:
            self.score = 0
            self.keep_playing = False
            print('You\'ve lost the game!')
        
    # This function is the interactive portion of the program.
    # Here we seek player input and display information to the player.
    def do_output(self):

        print(f'The card is {self.p_card}')
        # not sure if this input should be here, or in another place.
        user_input = input('Higher or lower? [h/l] ')
        # Also we should get the input of the user and pass that value to the compare_card,
        # that comes from the dealer.
        self.score += self.dealer.compare_card(user_input)

        if self.dealer.new_card > self.dealer.previous_card and user_input == "h":
            print(f'{Fore.GREEN}Next card was: {self.n_card}{Style.RESET_ALL}')
        elif self.dealer.new_card > self.dealer.previous_card and user_input == "l":
            print(f'{Fore.RED}Next card was: {self.n_card}{Style.RESET_ALL}')
        elif self.dealer.new_card < self.dealer.previous_card and user_input == "l":
            print(f'{Fore.GREEN}Next card was: {self.n_card}{Style.RESET_ALL}')
        elif self.dealer.new_card < self.dealer.previous_card and user_input == "h":
            print(f'{Fore.RED}Next card was: {self.n_card}{Style.RESET_ALL}')
        elif self.dealer.new_card == self.dealer.previous_card and user_input == "l":
            print(f'{Fore.YELLOW}Next card was: {self.n_card}{Style.RESET_ALL}')
        elif self.dealer.new_card == self.dealer.previous_card and user_input == "h":
            print(f'{Fore.YELLOW}Next card was: {self.n_card}{Style.RESET_ALL}')


        print(f'Your score is: {self.score}')

        playing = input('Keep playing? [y/n] ')

        # It may be possible it's necessary to adjust this. 
        # Maybe the dealer should handle if they can keep playing
        # since the score may be 0 and they could not be able to play anymore.
        if playing.lower() == 'y':
            self.keep_playing = True
        else:
            self.keep_playing = False
            print('Good bye baby!')

        print()