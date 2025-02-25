'''
Escreva uma função chamada avoids que receba uma palavra e uma série de letras proibidas, e retorne True se a palavra não usar nenhuma das letras proibidas.

Altere o código para que o usuário digite uma série de letras proibidas e o programa imprima o número de palavras que não contêm nenhuma delas. Você pode encontrar uma combinação de cinco letras proibidas que exclua o menor número possível de palavras?
'''

letters_banned = str(input('Enter with the letters banned: '))
with open('Books/pense_python/exercise9/moby_words.txt', 'r', encoding='utf-8') as file:
    txt = file.read()

def avoids(word = str(), letters_banned = str()):
    letters_banned = list(letters_banned)
    word = word.split()
    count_words = 0
    for actual_word in word: #take one word
        count_letters = 0
        for value in letters_banned: #take one letter in the letters banned
            if value not in actual_word:
                count_letters += 1
                if count_letters == len(letters_banned): #"Key" to "break" and analytics all letters
                    count_words += 1
                    print(actual_word)
    return count_words

print(avoids(txt, letters_banned))
