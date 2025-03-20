'''
b) Acrescente uma função ao programa anterior para gerar texto aleatório baseado na análise de Markov. Aqui está um exemplo de exemplo de Emma com o comprimento de prefixo 2.
He was very clever, be it sweetness or be angry, ashamed or only amused, at such a stroke. She had never thought of Hannah till you were never meant for me?” “I cannot make speeches, Emma:” he soon cut it all himself.
Para este exemplo, deixei a pontuação anexada às palavras. O resultado é quase sintaticamente correto, mas não exatamente. Semanticamente, quase faz sentido, mas não exatamente.
O que acontece se você aumentar o comprimento dos prefixos? O texto aleatório faz mais sentido?
'''

from exercise13_8_1 import get_pre_su
from random import choice, randint

words = list()

with open('Books/pense_python/exercise13/file13-7.txt', 'r', encoding='utf-8') as file:
    for x in file:
        x = (x.replace('"', '').replace('(','').replace(')','').split())
        for y in x:
            words.append(y)

dict_words = get_pre_su(words)

def random_txt(words_dict, lenght = 2, max_words = 50):
    pref = choice(list(words_dict.keys()))
    print(' '.join(pref), end=' ')
    for x in range(max_words - lenght):
        if pref not in words_dict:
            break
        next_word = choice(words_dict[pref])
        print(next_word, end=' ')
        pref = (*pref[1:], next_word)



random_txt(dict_words)