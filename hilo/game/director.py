from colorama import  Fore, Style
from game.dealer import Dealer

class Director():
    
    '''The responsibilites of the Director is to keep track of the score and control the 
    sequence of play.

    Attributes:
        keep_playing (bool): keeps running or finishes the game if the user want.
        score (int): the initial score.
        dealer (Dealer):  an instance of the class of objects known as Dealer.
        p_card (str): the previous card converted to str => 'Ace', 'Jack', 'Queen' or 'King'.
        n_card (str): the new card converted to str => 'Ace', 'Jack', 'Queen' or 'King'.
    '''

    def __init__(self):
        '''The class constructor.
        
        Args:
            self (Director): an instance of Director.
        '''

        self.keep_playing = True
        self.score = 300
        self.dealer = Dealer()
        self.p_card = ''
        self.n_card = ''


    def start_game(self):
        '''Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        '''

        while self.keep_playing:
            self.get_card()
            self.do_output()
            self.track_score()
            

    def get_card(self):
        '''Gets the cards at the beginning of each round of play.
        Also, it converts the numbers 1, 11, 12 an 13 to str
        respectively, because they are face cards.

        Args:
            self (Director): An instance of Director.
        '''


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

    def track_score(self):
        '''This function will track the score and see if the user
        loses the game or not.

        Args:
            self (Director): An instance of Director.
        '''
        
        if self.score <= 0:
            self.score = 0
            self.keep_playing = False
            print('You\'ve lost the game!')
        
    
    def do_output(self):
        '''This function is the interactive portion of the program.
        Here we seek player input and display information to the player.
        
        Args:
            self (Director): An instance of Director.
            '''

        print(f'The card is {self.p_card}')

        user_input = input('Higher or lower? [h/l] ')
       
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

        if playing.lower() == 'y':
            self.keep_playing = True
        else:
            self.keep_playing = False
            print('Good bye baby!')

        print()