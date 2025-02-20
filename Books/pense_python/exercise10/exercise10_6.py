'''
Duas palavras são anagramas se você puder soletrar uma rearranjando as letras da outra. Escreva uma função chamada is_anagram que tome duas strings e retorne True se forem anagramas.
'''

word1 = 'listen'
word2 = 'silent'
word3 = 'evil'

def is_anagram(word1, word2):
    return sorted(word1) == sorted(word2)

print(is_anagram(word1,word2))
