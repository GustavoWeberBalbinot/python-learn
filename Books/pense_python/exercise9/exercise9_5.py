'''
Escreva uma função chamada uses_all que receba uma palavra e uma série de letras obrigatórias e retorne True se a palavra usar todas as letras obrigatórias pelo menos uma vez. Quantas palavras usam todas as vogais (aeiou)? E que tal aeiouy?
'''

word1 = "education"  # Deve retornar True para "aeiou"
word2 = "hello"      # Deve retornar False para "aeiou"
word3 = "facetiously"  # Deve retornar True para "aeiouy"

required1 = "aeiou" #ã é á... not enter in the filter
required2 = "aeiouy"  

with open('Books/pense_python/exercise9/moby_words.txt', 'r', encoding='utf-8') as file:
    txt = file.read()


def uses_all(word = str(), letters = str()):
    letters = list(letters)
    word = word.split() #This part is so good to separate the archive in list to many strings
    for words in word: #This part is to get the string in the list
        for lt in letters:
            if lt not in words:
                return False
    return True

def count_uses_all(word = str(), letters = str()):
        count_True = 0
        word = word.split()
        for w in word:
            if uses_all(w, letters):
                  count_True += 1
        return count_True
             

print(count_uses_all(txt, required2))
