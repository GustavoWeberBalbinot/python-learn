'''
Acesse o Projeto Gutenberg (http://gutenberg.org) e baixe seu livro favorito em domínio público em formato de texto simples.
Altere seu programa do exercício anterior para ler o livro que você baixou, pulando as informações do cabeçalho no início do arquivo e processando o resto das palavras como antes.
Então altere o programa para contar o número total de palavras no livro e o número de vezes que cada palavra é usada.
Exiba o número de palavras diferentes usadas no livro. Compare livros diferentes de autores diferentes, escritos em eras diferentes. Que autor usa o vocabulário mais extenso?
'''
import string

my_archive = 'Books/pense_python/exercise13/file13-2.txt'

def read_archive(your_archive):
    with open(your_archive, 'r', encoding='utf-8') as file:
        key = 0
        txt = ''
        for line in file:
            if '*** END OF THE PROJECT GUTENBERG EBOOK' in line: #Skip the end "Header"
                break
            if key == 1:
                txt = txt + line
                continue
            if '*** START OF THE PROJECT GUTENBERG EBOOK' in line: #Skip the earlu "Header"
                key = 1
        return txt

def format_txt(t = str()):
    d = dict()
    d_words = dict()
    for itens in string.punctuation:
        itens = ord(itens) #Use Unicode to TRANSLATE
        d[itens] = None
    d[8220] = None #Unicode to “
    d[8221] = None #Unicode to ”
    t = t.translate(d)
    t = t.replace(' ', string.whitespace).replace(' \t', '').replace('\t', '').replace('-', '').replace('—', '')
    t = t.replace('\x0b\x0c', '') #\x0b\x0c === ♂♀
    t = t.lower()
    t = t.splitlines()
    for line in t:
        d_words[line] = d_words.get(line,0) + 1
    d_words.pop('')
    print(f'The amount of diferrent words is:{len(d_words)}')
    return d_words

txt = read_archive('Books/pense_python/exercise13/file13-2.txt')
format_txt(txt)