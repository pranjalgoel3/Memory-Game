'''Starts a game of blackjack using commandline argument inputs'''

import random
import time
import os
import deck

def get_card_number(i):
    '''Returns a string to print for the card # (aesthetic)'''
    if i > 9:
        return "    {}    ".format(i)
    return "    {}     ".format(i)

def get_val_to_print(value):
    '''Returns a string that can be printed for the value (aesthetic)'''
    if value == "10":
        return "|   10   |"

    return "|   {}    |".format(value)

def get_suit_to_print(suit):
    '''Returns a string that can be printed for the suit (aesthetic)'''
    if suit == "Hearts":
        return "| Hearts |"
    if suit == "Spades":
        return "| Spades |"
    if suit == "Clubs":
        return "| Clubs  |"
    if suit == "Diamonds":
        return "|Diamonds|"

    return ""

def show_cards(game_state, moves):
    '''Print out the game state and the cards to the console'''
    for i in range(0, 12, 3):
        card1 = game_state[i]['card']
        state1 = game_state[i]['selected'] or game_state[i]['solved']

        card2 = game_state[i+1]['card']
        state2 = game_state[i+1]['selected'] or game_state[i+1]['solved']

        card3 = game_state[i+2]['card']
        state3 = game_state[i+2]['selected'] or game_state[i+2]['solved']

        val1 = get_val_to_print(card1.value) if state1 else "|   ?    |"
        val2 = get_val_to_print(card2.value) if state2 else "|   ?    |"
        val3 = get_val_to_print(card3.value) if state3 else "|   ?    |"

        suit1 = get_suit_to_print(card1.suit) if state1 else "|   ?    |"
        suit2 = get_suit_to_print(card2.suit) if state2 else "|   ?    |"
        suit3 = get_suit_to_print(card3.suit) if state3 else "|   ?    |"


        print(" -------- " + "    " + " -------- " + "    " + " -------- ")
        print("|        |" + "    " + "|        |" + "    " + "|        |")
        print(val1 + "    " + val2 + "    " + val3)
        print(suit1 + "    " + suit2 + "    " + suit3)
        print("|        |" + "    " + "|        |" + "    " + "|        |")
        print(" -------- " + "    " + " -------- " + "    " + " -------- ")
        print(get_card_number(i+1) + "    " +
              get_card_number(i+2) + "    " +
              get_card_number(i+3))
        print()

    print("Num of moves: " + str(moves))


def main():
    '''Runs the game'''
    game_deck = deck.Deck() # Get a deck of cards
    cards_chosen = [] # a list to draw 6 cards

    # Draw 6 cards from the deck
    for _ in range(6):
        card = game_deck.draw_card()
        cards_chosen.append(card)
        cards_chosen.append(card)

    # Shuffle them to make sure same 2 cards don't exist together
    random.shuffle(cards_chosen)

    game_state = {} # Stores the state of the game
    for idx, card in enumerate(cards_chosen):
        game_state[idx] = {'card': card, 'solved': False,
                           'selected': False}

    num_moves = 0 # Track of number of moves
    num_remaning_matches = 6

    print("***************************************************")
    print("*****      Welcome to Memory Game!           ******")
    print("***** Select cards between 1-12 and proceed! ******")
    print("***************************************************")
    print()

    while num_remaning_matches > 0:
        show_cards(game_state, num_moves)

        card1 = input("\nSelect first card: ")
        card2 = input("Select second card: ")

        # Check to see if the input is an integer
        # If it is, convert it
        try:
            card1 = int(card1) - 1
            card2 = int(card2) - 1
        except ValueError:
            print("Please enter an integer between 1-12 to select a card")
            continue
        except:
            print("Exiting due to unexpected input")
            break

        # If the card is out of range, ask again
        if card1 < 0 or card1 > 11 or card2 < 0 or card2 > 11 or card1 == card2:
            print("Invalid card selection. Please select a card between 1-12")
            continue

        # If card chosen is already solved, pick again
        if game_state[card1]['solved'] or game_state[card2]['solved']:
            print("Please select cards which haven't been seen before")
            continue

        num_moves += 1

        # Check if the cards selected are the same
        if game_state[card1]['card'] == game_state[card2]['card']:
            num_remaning_matches -= 1
            game_state[card1]['solved'] = True
            game_state[card2]['solved'] = True

            show_cards(game_state, num_moves)
            os.system('clear && printf \'\\e[3J\'')
        # If the cards are not the same
        else:
            game_state[card1]['selected'] = True
            game_state[card2]['selected'] = True

            show_cards(game_state, num_moves)

            game_state[card1]['selected'] = False
            game_state[card2]['selected'] = False

            time.sleep(4)
            os.system('clear && printf \'\\e[3J\'')

        if num_remaning_matches == 0:
            print("You win!")
            print("Num of moves: " + str(num_moves))
            break

if __name__ == '__main__':
    main()
