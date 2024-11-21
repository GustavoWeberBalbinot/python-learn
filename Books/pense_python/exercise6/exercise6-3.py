#Escreva uma função chamada is_palindrome que receba uma string como argumento e retorne True se for um palíndromo e False se não for. Lembre-se de que você pode usar a função integrada len para verificar o comprimento de uma string.

def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    return word[1:-1]


def middle_backwards(word):
    teste = ''
    for x in range(len(word)-2,0, -1):
        teste += word[x]
    return teste


def is_palindrome(word):
    if first(word) == last(word) and middle(word) == middle_backwards(word):
        a = 'This is a palindrome'
        return a
    else:
        a = 'This is not a palindrome'
        return a

print(is_palindrome('radar'))
