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
    random_numb = randint(1,len(t_frequence))
    value_random = binary_search(t_acumulate_frequence, t_acumulate_frequence[random_numb])
    print(value_random)
    word = t_words[value_random]
    return word


def binary_search(list_numbs, value_to_search = 0):
    high_value= len(list_numbs) - 1
    lower_value = 0
    while lower_value <= high_value:
        middle_value = (lower_value + high_value)
        if value_to_search == list_numbs[middle_value]:
            return middle_value
        if value_to_search > list_numbs[middle_value]:
            lower_value = middle_value + 1
        else:
            high_value = middle_value - 1


print(random_word(all_values_dict))
print('a')