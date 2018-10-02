'''This class creates a Deck of Cards and the deck is returned as a
shuffled list
'''
from random import shuffle

class Deck:
    '''Thsi class mainatains a standard deck of cards and supports
    removing a card when required'''
    def __init__(self):
        '''Inintializes the deck with 52 cards (shuffled)'''
        self.deck = []
        Deck.reset_deck(self)
        Deck.shuffle(self)

    def reset_deck(self):
        '''Resets the deck with 52 cards'''
        suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
        values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "A", "J",
                  "Q", "K"]

        self.deck = []

        for suit in suits:
            for val in values:
                card = Card(val, suit)
                self.deck.append(card)

    def shuffle(self):
        '''Shuffles the cards in the deck'''
        shuffle(self.deck)

    def draw_card(self):
        '''Removes a card from the deck and returns it'''
        if not self.deck:
            return None

        return self.deck.pop(0)

class Card:
    '''This class is used for representation of a playing card with a
    value and a suit associated with it'''
    def __init__(self, val, suitName):
        '''Initializes the card with a value and a suit.
        Raises a value error if either are null or not correct.
        '''
        suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
        if suitName is None or suitName not in suits:
            raise ValueError("Invalid suit name!")

        values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "A", "J",
                  "Q", "K"]
        if val is None or val not in values:
            raise ValueError("Invalid value!")

        self.value = val
        self.suit = suitName

    def __eq__(self, card2):
        return self.value == card2.value and self.suit == card2.suit

    def __str__(self):
        return self.value + " of " + self.suit


def main():
    '''Generates a new deck of cards and prints the cards'''
    deck = Deck()
    for card in deck.deck:
        print(card)

if __name__ == '__main__':
    main()
