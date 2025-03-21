'''
A “classificação” de uma palavra é a sua posição em uma lista de palavras classificadas por frequência: a palavra mais comum tem a classificação 1, a segunda mais comum é 2 etc.

A lei de Zipf descreve a relação entre classificações e frequências das palavras em linguagens naturais (http://en.wikipedia.org/wiki/Zipf’s_law). Ela prevê especificamente que a frequência, f, da palavra com classificação r é:

f = cr−s
onde s e c são parâmetros que dependem do idioma e do texto. Se você tomar o logaritmo de ambos os lados desta equação, obtém:

log f = log c − s log r
Se você traçar o log de f contra o log de r, terá uma linha reta com uma elevação -s e interceptar o log de c.

Escreva um programa que leia um texto em um arquivo, conte as frequências das palavras e exiba uma linha para cada palavra, em ordem descendente da frequência, com log de f e log de r. Use o programa gráfico de sua escolha para traçar os resultados e verifique se formam uma linha reta. Você pode estimar o valor de s?
'''

import matplotlib.pyplot as plt
import numpy as np

words = dict()
teste = list()

with open('Books/pense_python/exercise13/file13-8-3_2.txt', 'r', encoding='utf-8' ) as file:
    for x in file:
        x = (x.replace('"', '').replace('(','').replace(')','').lower().split())
        for y in x:
            if y not in words:
                words[y] = 0
            words[y] = words.get(y,0) + 1

for key, value in words.items():
    a = value, key
    teste.append(a)
teste = sorted(teste, reverse=True)

frequence = list()
words_list = list()

for x in range(len(teste)):
    frequence.append(teste[x][0])
    words_list.append(x)



log_f = np.log(frequence)
log_r = np.log(words_list)

