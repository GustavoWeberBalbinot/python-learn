'''
Duas palavras são “pares rotacionados” se for possível rotacionar um deles e chegar ao outro (ver rotate_word no Exercício 8.5).

Escreva um programa que leia uma lista de palavras e encontre todos os pares rotacionados.
'''

list_words = ['cheer', 'melon', 'jolly', 'cubed', 'noneword']

def rotate_word(word='', numb=0):
    if numb == 0:
        word
    new_word = ''
    for letter in word:
        base = ord('A') if letter.isupper() else ord('a')
        numb_actual = ((ord(letter) - base) + numb) % 26
        new_word += chr(base + numb_actual)
    return new_word

def pair_rotate_words(list_itens):
    d = dict()
    for itens in list_itens:
        cont = 0
        for numb in range(1,26):
            new_word = rotate_word(itens, numb)
            if new_word in list_itens:
                d[itens] = [new_word, numb]
                cont += 1
            if numb == 25 and cont == 0:
                d[itens] = False
    return d

print(pair_rotate_words(list_words))