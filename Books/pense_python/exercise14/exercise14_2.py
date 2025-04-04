'''
Se você baixar minha solução do Exercício 12.2 em http://thinkpython2.com/code/anagram_sets.py, verá que ela cria um dicionário que mapeia uma string ordenada de letras à lista de palavras que podem ser soletradas com aquelas letras. Por exemplo, 'opst' mapeia à lista ['opts', 'post', 'pots', 'spot', 'stop', 'tops'].

Escreva um módulo que importe anagram_sets e forneça duas novas funções: store_anagrams deve guardar o dicionário de anagramas em uma “prateleira” (objeto criado pelo módulo sheve); read_anagrams deve procurar uma palavra e devolver uma lista dos seus anagramas.
'''

import nltk
from nltk.corpus import words


def exist_word(palavra):
    return palavra.lower() in words.words()



def letters_to_anagram(letters):
    list_words = list()
    all_words = list()
    letters = sorted(letters)
    new_word = letters[:]
    for x in range(len(letters) - 1):
        new_word = letters[:]
        for y in range(len(letters) - 1):
            new_word.pop(x + y)
            new_word.insert(y + x +1,letters[x])
            if new_word in all_words:
                continue
            else:
                all_words.append(new_word)
    return all_words





def main(letters):
    print('a')



if __name__ == "__main__":
    letters = str(input('Enter with the letters: '))
    print(letters_to_anagram(letters))
