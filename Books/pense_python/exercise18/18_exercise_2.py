'''
Escreva um método Deck chamado deal_hands que receba dois parâmetros: o número de mãos e o número de cartas por mão. Ele deve criar o número adequado de objetos Hand, lidar com o número adequado de cartas por mão e retornar uma lista de Hands.
'''

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

    def deal_hands(n_hands = 1, n_cards = 7):
        h = []
        count = 0
        for x in n_hands:
            count += 1
            actual_hand = count
            for n in n_cards:
                h.append(actual_hand = Hand())


class Hand(Card):
    pass

deck = Deck()
print(deck)