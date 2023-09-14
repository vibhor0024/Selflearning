# Blackjack rules
# to have hands total higher than the dealer but not more than 21 (bust)
# if bust happens, you are out of the game
# everyone besides the dealer places a bet
# the dealer deals 1 card face up to each player and themselves
# everyone is dealt one more face up card besides the dealer, whose 2nd card is face down
# cards 2-10 hold their face value and K,Q,J are all equal to 10
# A can be 1 or 11
# If 2 cards of any player add up to 21 they automatically win 1.5 times their bet from the dealer
# and are done for that round
# otherwise dealer asks if you want another card from the top of the deck
# if you want more cards say hit
# you can get any number of cards but if it's a bust dealer gets your money
# If you do not want any more card say stay
# after that the dealer filps their face down card
# if it's 16 or under they have to pick another card
# if it's 17 or higher they have to stay with their hand
# if the dealer busts, every player still in the round gets twice their bet
# if the dealer does not bust, players whose hands are higher than the dealer's win twice their bet
# everone else loses their initial bet
# then new round begins with new bets

import random


class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return f'{self.rank["rank"]} of {self.suit}'



class Deck:

    def __init__(self):
        suits = ['spades','clubs','hearts','diamonds']

        ranks = [{'rank':'A','value':11},
                {'rank':2,'value':2},
                {'rank':3,'value':3},
                {'rank':4,'value':4},
                {'rank':5,'value':5},
                {'rank':6,'value':6},
                {'rank':7,'value':7},
                {'rank':8,'value':8},
                {'rank':9,'value':9},
                {'rank':10,'value':10},
                {'rank':'J','value':10},
                {'rank':'Q','value':10},
                {'rank':'K','value':10}]
        
        self.cards =[]

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit,rank))

    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self,number):
        cards_dealt = []
        for i in range(number):
            if len(self.cards)>0:
                card = self.cards.pop()
                cards_dealt.append(card)
        return cards_dealt

class Hand:

    def __init__(self,dealer = False):
        self.cards = []
        self.value = 0
        self.dealer = dealer
    
    def add_cards(self,card_list):
        self.cards.extend(card_list)
    
    def calculate_value(self):
        self.value = 0
        has_ace = False

        for card in self.cards:
            card_value = int(card.rank['value'])
            self.value += card_value
            if card.rank['rank'] == 'A':
                has_ace = True
        
        if has_ace and self.value > 21:
            self.value -= 10
    
    def get_value(self):
        self.calculate_value()
        return self.value
    
    def is_blackjack(self):
        return self.get_value() == 21
    
    def display(self,show_dealer_cards = False):
        print(f"""\n{"Dealer's" if self.dealer else "Your"} hand: \n""")

        for index,card in enumerate(self.cards):
            if index == 0 and self.dealer and \
            not show_dealer_cards and not self.is_blackjack():
                print('hidden')
            else:
                print(card)

        if not self.dealer:
            print(f'value: {self.get_value()}\n')

class Game:

    def play(self):
        game_number = 0
        games_to_play = 0

        while games_to_play <= 0:
            try:
                games_to_play = int(input("How many games do you want to play? "))
            except:
                print("You must enter a number.")

        while game_number < games_to_play:
            game_number += 1

            deck = Deck()
            deck.shuffle()

            player_hand = Hand()
            dealer_hand = Hand(dealer=True)

            for i in range(2):
                player_hand.add_cards(deck.deal(1))
                dealer_hand.add_cards(deck.deal(1))

            print()
            print("*" * 30)
            print(f"Game {game_number} of {games_to_play}")
            print("*" * 30)
            player_hand.display()
            dealer_hand.display()

            if self.check_winner(player_hand, dealer_hand):
                continue

            choice = ""
            while player_hand.get_value() < 21 and choice not in ["s", "stay"]:
                choice = input("Please choose 'Hit' or 'Stay': ").lower()
                print()
                while choice not in ["h", "s", "hit", "stay"]:
                    choice = input("Please enter 'Hit' or 'Stay' (or H/S) ").lower()
                    print()
                if choice in ["hit", "h"]:
                    player_hand.add_cards(deck.deal(1))
                    player_hand.display()
                    
            if self.check_winner(player_hand, dealer_hand):
                continue

            player_hand_value = player_hand.get_value()
            dealer_hand_value = dealer_hand.get_value()

            while dealer_hand_value < 17:
                dealer_hand.add_cards(deck.deal(1))
                dealer_hand_value = dealer_hand.get_value()

            dealer_hand.display(show_dealer_cards=True)

            if self.check_winner(player_hand, dealer_hand):
                continue

            print("Final Results")
            print("Your hand:", player_hand_value)
            print("Dealer's hand:", dealer_hand_value)

            self.check_winner(player_hand, dealer_hand, True)

        print("\nThanks for playing!")


    def check_winner(self, player_hand, dealer_hand, game_over = False):
        
        if not game_over:

            if player_hand.get_value() > 21:
                print('You busted, Dealer wins')
                return True
            
            elif dealer_hand.get_value() > 21:
                print('Dealer busted, you win')
                return True

            elif dealer_hand.is_blackjack() and player_hand.is_blackjack():
                print("Both have a blackjack, it's a tie")
                return True

            elif dealer_hand.is_blackjack():
                print("Dealer has a blackjack, he wins")
                return True 

            elif player_hand.is_blackjack():
                print("You have a blackjack, you win")
                return True   
             
        else:

            if player_hand.get_value() > dealer_hand.get_value():
                print('You win')         

            elif dealer_hand.get_value() > player_hand.get_value():
                print('Dealer wins')

            else:
                print("It's a tie")
            
            return True
    
        return False


game = Game()
game.play()
