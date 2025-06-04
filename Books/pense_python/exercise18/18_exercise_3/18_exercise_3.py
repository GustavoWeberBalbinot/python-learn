'''
A seguir, as mãos possíveis no pôquer, em ordem crescente de valor e ordem decrescente de probabilidade:

Par: Duas cartas com o mesmo valor.
Dois pares: Dois pares de cartas com o mesmo valor.
Trinca:Três cartas com o mesmo valor.
Sequência:Cinco cartas com valores em sequência (os ases podem ser altos ou baixos, então Ace-2-3-4-5 é uma sequência, assim como 10-Jack-Queen-King-Ace, mas Queen-King-Ace-2-3 não é.)
Flush:Cinco cartas com o mesmo naipe.
Full house:Três cartas com um valor, duas cartas com outro.
Quadra:Quatro cartas com o mesmo valor.
Straight flush:Cinco cartas em sequência (como definido acima) e com o mesmo naipe.
A meta desses exercícios é estimar a probabilidade de ter estas várias mãos.

Baixe os seguintes arquivos de http://thinkpython2.com/code:
Card.py: Versão completa das classes Card, Deck e Hand deste capítulo.

PokerHand.py: Uma implementação incompleta de uma classe que representa uma mão de pôquer e código para testá-la.

Se executar PokerHand.py, você verá que o programa cria mãos de pôquer com 7 cartas e verifica se alguma delas contém um flush. Leia este código com atenção antes de continuar.

Acrescente métodos a PokerHand.py chamados has_pair, has_twopair, etc. que retornem True ou False conforme a mão cumpra os critérios em questão. Seu código deve funcionar corretamente para “mãos” que contenham qualquer número de cartas (embora 5 e 7 sejam as quantidades mais comuns).

Escreva um método chamado classify que descubra a classificação do valor mais alto para uma mão e estabeleça o atributo label em questão. Por exemplo, uma mão de 7 cartas poderia conter um flush e um par; ela deve ser marcada como “flush”.

Quando se convencer de que os seus métodos de classificação estão funcionando, o próximo passo deve ser estimar as probabilidades de várias mãos. Escreva uma função em PokerHand.py que embaralhe cartas, divida-as em mãos, classifique as mãos e conte o número de vezes em que várias classificações aparecem.

Exiba uma tabela das classificações e suas probabilidades. Execute seu programa com números cada vez maiores de mãos até que os valores de saída convirjam a um grau razoável de exatidão. Compare seus resultados com os valores em http://en.wikipedia.org/wiki/Hand_rankings.
'''

"""
This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey
License: http://creativecommons.org/licenses/by/4.0/

Modificações por Gustavo Weber Balbinot
Adicionado em 2025: novas funções e melhorias para estudo pessoal.
Você pode usar e modificar este código desde que mantenha esta nota de atribuição.
"""


from Card import Hand, Deck


class PokerHand(Hand):
    """Represents a poker hand."""

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1
            
    def rank_hist(self):
        """Buids a histogram of the ranks that appear in the hand.
        
        Store the result in attribute ranks.
        """
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1
        
    def sort_rank(self):
        self.ordened_rank = ()
        self.ordened_rank = sorted(self.cards, key=lambda card: card.rank)

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False
    
    def has_pair(self):
        """ Returns True if the hand has a pair, False otherwise

        Note that this works correctly if hand with more 2 cards.
        """
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 2:
                return True
        return False

    def has_two_pair(self):
        """Returns True if the hand has two pair, False otherwise

        Note that this works correctly if hand with more 4 cards.
        """
        self.rank_hist()
        pair_count = 0
        for val in self.ranks.values():
            if val >= 2:
                pair_count += 1
            if pair_count >= 2:
                return True
        return False

    def has_three_of_a_kind(self):
        """Return True if the hand has a three of a kind card, False otherwise
        
        Note that this work correctly if hand with more 3 cards.
        """
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 3:
                return True
        return False

    def has_sequence(self):
        """Return True if the amount of 5 cards has a sequence, False otherwise
        
        Note that this work correctly if hand with more 5 cards. Ace count as 1 and 14
        """
        self.sort_rank()
        for x in self.ordened:
            print(x)

if __name__ == '__main__':
    # make a deck
    deck = Deck()
    deck.shuffle()

    # deal the cards and classify the hands
    for i in range(7):
        hand = PokerHand()
        deck.move_cards(hand, 7)
        hand.sort()
        print(hand)
        print(hand.has_sequence())
        print('')