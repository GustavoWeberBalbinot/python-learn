'''
b) Acrescente uma função ao programa anterior para gerar texto aleatório baseado na análise de Markov. Aqui está um exemplo de exemplo de Emma com o comprimento de prefixo 2.
He was very clever, be it sweetness or be angry, ashamed or only amused, at such a stroke. She had never thought of Hannah till you were never meant for me?” “I cannot make speeches, Emma:” he soon cut it all himself.
Para este exemplo, deixei a pontuação anexada às palavras. O resultado é quase sintaticamente correto, mas não exatamente. Semanticamente, quase faz sentido, mas não exatamente.
O que acontece se você aumentar o comprimento dos prefixos? O texto aleatório faz mais sentido?
'''

from exercise13_8_1 import get_pre_su
from random import choice

words = list()

with open('Books/pense_python/exercise13/file13-7.txt', 'r', encoding='utf-8') as file:
    for x in file:
        x = (x.replace('"', '').replace('(','').replace(')','').split())
        for y in x:
            words.append(y)

dict_words = get_pre_su(words)

def random_txt(words_dict, lenght = 2):
    count = lenght - lenght
    for key, value in words_dict.items():
        if count % (lenght+1) == 0:
            for x in range(len(key)):
                print(f'{key[x]} ', end='')
            print(f'{choice(value)} ', end='')
        count += 1
        



random_txt(dict_words)