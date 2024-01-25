import random

class Card(object):
    def __init__(self, value, suit):
            self.value = value
            self.suit = suit
            self.showing = True
    
    def __repr__(self):
        VALUE_NAMES = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
        SUIT_NAMES = ["Spades", "Clubs", "Diamonds", "Hearts"]

        value_name = VALUE_NAMES[self.value]
        suit_name = SUIT_NAMES[self.suit]
        return f"{value_name} of {suit_name}"

class StandardDeck(list):
    def __init__(self):
        super().__init__()
        self.generate_deck()

    def generate_deck(self):
        '''Creates a standard 52-card deck'''
        suits = list(range(4))
        values = list(range(13))
        [[self.append(Card(value, suit)) for value in values] for suit in suits]
        # ^-- creating deck with ace to king per suit --> deck will be in order
    
    def shuffle(self):
        '''Shuffles the deck into a random order'''
        random.shuffle(self)

    def deal(self, location):
        ''' Deals the next card from the deck'''
        location.cards.append(self.pop(0)) 
    
    def reset_deck(self):
        '''Resets the deck and creates a new one (The deck is in order when created)'''
        self.clear()
        self.generate_deck()
        
        
deck = StandardDeck()