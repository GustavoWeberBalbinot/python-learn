'''
Exercício 13.7
Escreva um programa que escolha uma palavra aleatória do livro.
'''

from exercise13_2 import format_txt, read_archive
from random import randint

my_archive = 'Books/pense_python/exercise13/file13-2.txt'

txt = read_archive(my_archive)
all_values_dict = format_txt(txt) #This function get the words and the frequence.

def random_word(txt):
    n = 0
    t_words = list()
    t_frequence = list()
    t_acumulate_frequence = list()
    for key, value in txt.items():
        t_words.append(key)
        t_frequence.append(value)
    t_frequence = sorted(t_frequence)
    for value in t_frequence:
        t_acumulate_frequence.append(n + value)
        n += value
    random_numb = randint(1,t_acumulate_frequence[-1])
    value_random = binary_search(t_acumulate_frequence, random_numb)
    print(value_random)
    teste = t_words[value_random]
    return teste


def binary_search(list_numbs, value_to_search = 0):
    high_position = len(list_numbs)
    actual_position = high_position // 2
    lower_position = 0
    while lower_position <= high_position:
        actual_position = (lower_position + high_position) // 2
        if list_numbs[actual_position] == value_to_search:
            return actual_position
        elif value_to_search > list_numbs[actual_position]:
            lower_position = actual_position + 1
        else:
            high_position = actual_position - 1



print(random_word(all_values_dict))
print('a')