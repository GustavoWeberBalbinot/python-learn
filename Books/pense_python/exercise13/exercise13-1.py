'''
Escreva um programa que leia um arquivo, quebre cada linha em palavras, remova os espaços em branco e a pontuação das palavras, e as converta em letras minúsculas.

Dica: O módulo string oferece uma string chamada whitespace, que contém espaço, tab, newline etc., e punctuation, que contém os caracteres de pontuação. Vamos ver se conseguimos fazer o Python falar palavrões:
'''

import string

with open('Books/pense_python/exercise13/file13-1.txt', 'r') as file:
    txt = file.read()

def format_txt(t = str()):
    all_punctuation = list(string.punctuation)
    t = t.replace(' ', string.whitespace)
    t = t.replace('\x0b\x0c', '') #\x0b\x0c === ♂♀
    for iten in all_punctuation:
        t = t.replace(iten, '')
    t = t.lower()
    return t


format_txt(txt)
