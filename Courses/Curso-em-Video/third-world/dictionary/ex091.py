#Leia 4 input de 4 jogadores, onde vão jogar um dado
#Guarde - os resultados no dicionário
#Mostre - em ordem, o vencedor - quem tirou o maior dado

from random import randint
from operator import itemgetter
temp_dictionary = dict()
player_list = list()

for x in range(0,4):
    numb_dice = randint(1,6)
    temp_dictionary[f'player {x + 1}'] = numb_dice
    print(f'The player {x + 1}, got:', numb_dice)

player_list = sorted(temp_dictionary.items(), key=itemgetter(1), reverse=True)

for p,v in player_list:
    print(f'The player {p} got: {v}')