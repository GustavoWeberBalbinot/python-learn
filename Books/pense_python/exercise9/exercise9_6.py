'''
Escreva uma função chamada is_abecedarian que retorne True se as letras numa palavra aparecerem em ordem alfabética (tudo bem se houver letras duplas). Quantas palavras em ordem alfabética existem?
'''

#I don't want to use sorted in the word because it would be too easy

with open('Books/pense_python/exercise9/moby_words.txt', 'r', encoding='utf-8') as file:
    txt = file.read()

teste1 = 'abcde'
teste2 = 'bcdea'

def is_abecedarian(word = str()):
    word = word.split()
    last_letter = 0
    for w in word:
        w = w.lower()
        for letters in w:
            letters = ord(letters)
            if letters >= last_letter:
                last_letter = letters
            else:
                return False
    return True

def count_is_abecedarian(word = str()):
    word = word.split()
    count_abcedarian = 0
    for w in word:
        if is_abecedarian(w):
            count_abcedarian += 1
    return count_abcedarian

print(count_is_abecedarian(txt))

