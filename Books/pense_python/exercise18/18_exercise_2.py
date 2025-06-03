'''
Escreva um método Deck chamado deal_hands que receba dois parâmetros: o número de mãos e o número de cartas por mão. Ele deve criar o número adequado de objetos Hand, lidar com o número adequado de cartas por mão e retornar uma lista de Hands.
'''

from random import randint

class Card():
    '''Reference a card of the poker game
    attributes: suit, rank
    '''

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7','8', '9', '10', 'Jack', 'Queen', 'King']


    def __init__(self, suit=0, rank=1):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.suit_names[self.suit]} of {self.rank_names[self.rank]}'
    
    def __lt__(self, other):
        c1 = self.suit, self.rank
        c2 = other.suit, other.rank
        return c1 < c2


class Deck():
    '''Reference a One Deck of cards, in the poker game
    attributes: cards
    '''

    def __init__(self):
        self.cards = []
        for x in range(4):
            for y in range(1,14):
                card = Card(x,y)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return f'\n'.join(res)

    def random_card(self):
        return randint(0,len(self.cards) - 1)

    def add_card(self, card):
        self.cards.append(card)
    
    def remove_card(self,card):
        self.cards.remove(card)

    def deal_hands(self, n_hands = 1, n_cards = 7):
        if n_cards * n_cards > len(self.cards):
            print(f'The deck have 52 cards, and the amount of players exceeds this limit')
            return False
        h = []
        for actual_hand in range(n_hands):
            hand = Hand()
            for y in range(n_cards):
                r_card = self.random_card() 
                hand.add_card(self.cards[r_card])
                self.remove_card(self.cards[r_card])
            h.append((hand))
        return h    
        


class Hand():
    '''Reference a group of cards
    attributes: hand
    '''

    def __init__(self, card = None):
        if card is None:
            self.card = []
        else:
            self.card = card
    
    def add_card(self, card):
        self.card.append(card)

    def __str__(self):
        res = []
        for card in self.card:
            res.append(str(card))
        return f'\n'.join(res)


def print_hands(hands):
    for i, hand in enumerate(hands, start=1):
        print(f'\nHand {i}:')
        print(hand)


deck = Deck()
hands = deck.deal_hands(2, 7)
print_hands(hands)
