'''
O Python fornece uma estrutura de dados chamada SET, que fornece muitas operações de conjunto. Você pode ler sobre elas em “Conjuntos”, na página 274, ou ler a documentação em http://docs.python.org/3/library/stdtypes.html#types-set.

Escreva um programa que use a subtração de conjuntos para encontrar palavras no livro que não estão na lista de palavras.
'''

import string


def read_archive(file_name, book_gunterberg = False):
    hist = dict()
    file = open(file_name, 'r', encoding='utf-8')
    if book_gunterberg:
        for line in file:
            if '*** START OF THE PROJECT GUTENBERG EBOOK' in line:
                break
    for line in file:
        analitic_line(line, hist)
    file.close()
    return hist

def analitic_line(line,hist):
    line = line.replace('-', '')
    for word in line.split():
         word = word.strip(string.punctuation + string.whitespace )
         word = word.lower()
         hist[word] = hist.get(word,0) + 1


def compare_archives(file1,file2):
    hist = dict()
    for key in file1:
         if key not in file2:
              hist[key] = None
    return hist.keys()

file1 = read_archive('Books/pense_python/exercise13/file13-2.txt', book_gunterberg=True)
file2 = read_archive('Books/pense_python/exercise13/moby_words.txt')
print(compare_archives(file1,file2))
