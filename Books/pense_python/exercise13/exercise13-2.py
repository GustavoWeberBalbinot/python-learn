'''
Acesse o Projeto Gutenberg (http://gutenberg.org) e baixe seu livro favorito em domínio público em formato de texto simples.
Altere seu programa do exercício anterior para ler o livro que você baixou, pulando as informações do cabeçalho no início do arquivo e processando o resto das palavras como antes.
Então altere o programa para contar o número total de palavras no livro e o número de vezes que cada palavra é usada.
Exiba o número de palavras diferentes usadas no livro. Compare livros diferentes de autores diferentes, escritos em eras diferentes. Que autor usa o vocabulário mais extenso?
'''
import string

with open('Books/pense_python/exercise13/file13-2.txt', 'r', encoding='utf-8') as file:
    for line in file:
        if '*** START OF THE PROJECT GUTENBERG EBOOK' in line:
            break
    txt = file.read()


def format_txt(t = str()):
    d = dict()
    d_words = dict()
    for itens in string.punctuation:
        itens = ord(itens) #Use Unicode to TRANSLATE
        d[itens] = None
    t = t.translate(d)
    t = t.replace(' ', string.whitespace).replace(' \t', '')
    t = t.replace('\x0b\x0c', '') #\x0b\x0c === ♂♀
    t = t.lower()
    t = t.splitlines()
    for line in t:
        d_words[line] = d_words.get(line,0) + 1
    d_words.pop('')
    return d_words


print(format_txt(txt))
