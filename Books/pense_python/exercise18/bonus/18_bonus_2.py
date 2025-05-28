'''
Como exercício, escreva um método de Deck chamado sort, que use o método de lista sort para classificar as cartas em um Deck. sort usa o método __lt__ que definimos para determinar a ordem.
'''

class Card():
    '''Cards in the pocker game
    attributes: suit, rank
    '''
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7','8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self,suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __lt__(self, other):
        c1 = (self.suit, self.rank)
        c2 = (other.suit, other.rank)
        return c1 < c2

    def __str__(self):
        return f'{self.suit_names[self.suit]} of {self.rank_names[self.rank]}'


class Deck():
    '''Deck of cards in the pocker game
    attributes: deck
    '''

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range (1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
    
    def sort(self):
        self.cards.sort(reverse=True)
        return self.cards
    
'''    def my_sort(self, reverse = False):
        res = []
        for x in self.cards:
            if not res:
               res.append(x)
            else:
               inserted = False
               for i in range(len(res)):
                   if (not reverse and x < res[i]) or (reverse and x > res[i]):
                        res.insert(i,x)
                        inserted = True
                        break
                   if not inserted:
                       res.append(x)
        self.cards = res[:]
        return self.cards'''


deck = Deck()
deck.sort()
print(deck)
