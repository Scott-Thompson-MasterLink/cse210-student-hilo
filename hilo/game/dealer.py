import random
from typing import NewType

class Dealer:
    '''The responsibilites of the dealer is to track and generate cards, determine score for the guess.

    Attributes:
        previous_card (int): previous card value
        new_card (int): the new card value

    '''

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Dealer): an instance of Dealer.
        """
        self.previous_card = 7
        self.new_card = 7


    def deal_card(self):
        '''Will reassign previous card value and genrate new card value

        Args:
            self (Dealer): an instance of Dealer.
        '''
        self.previous_card = self.new_card
        self.new_card = random.randint(1,13)



    def compare_card(self, guess):
        '''Will compare previous card with new card and will return score.

        Args:
            self (Dealer): an instance of Dealer.
            guess (str): player guess
        
        '''

        if guess.lower() == 'h':
            if self.previous_card < self.new_card:
                return 100
            elif self.previous_card >= self.new_card:
                return -75
        
        elif guess.lower() == 'l':
            if self.previous_card > self.new_card:
                return 100
            elif self.previous_card <= self.new_card:
                return -75
