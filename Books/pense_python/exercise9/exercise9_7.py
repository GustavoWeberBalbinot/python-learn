'''
Dê uma palavra com três letras duplas consecutivas. Vou dar exemplos de palavras que quase cumprem a condição, mas não chegam lá. Por exemplo, a palavra committee, c-o-m-m-i-t-t-e-e. Seria perfeita se não fosse aquele 'i' que se meteu ali no meio. Ou Mississippi: M-i-s-s-i-s-s-i-p-p-i. Se pudesse tirar aqueles 'is', daria certo. Mas há uma palavra que tem três pares consecutivos de letras e, que eu saiba, pode ser a única palavra que existe. É claro que provavelmente haja mais umas 500, mas só consigo pensar nessa. Qual é a palavra?

Escreva um programa que a encontre.
'''

with open('Books/pense_python/exercise9/moby_words.txt', 'r', encoding='utf-8') as file:
    txt = file.read()

word1 = 'commtteess' #teste word
word2 = 'committee'


def three_consecutive_double_letters(word = str()):
    word = word.lower()
    sequence_pair = 0
    i = 0
    while i < len(word) - 1:
        if word[i] == word[i + 1]:
            sequence_pair += 1
            i += 2
            if sequence_pair >= 3:
                print(word)
                return
        else:
            sequence_pair = 0
            i += 1
        


for words in txt:
    txt = txt.split()
    three_consecutive_double_letters(words)
