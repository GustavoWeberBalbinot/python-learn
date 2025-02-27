'''
Escreva uma função chamada uses_all que receba uma palavra e uma série de letras obrigatórias e retorne True se a palavra usar todas as letras obrigatórias pelo menos uma vez. Quantas palavras usam todas as vogais (aeiou)? E que tal aeiouy?
'''

word1 = "education"  # Deve retornar True para "aeiou"
word2 = "hello"      # Deve retornar False para "aeiou"
word3 = "facetiously"  # Deve retornar True para "aeiouy"

required1 = "aeiou"
required2 = "aeiouy"


def uses_all(word, letters):
    letters = list(letters)
    for lt in letters:
        if lt not in word:
            return False
    return True


print(uses_all(word2, required1))
