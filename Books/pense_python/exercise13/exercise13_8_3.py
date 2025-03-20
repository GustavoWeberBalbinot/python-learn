'''
c) Uma vez que o seu programa esteja funcionando, você pode querer tentar uma mistura: se combinar o texto de dois ou mais livros, o texto aleatório gerado misturará o vocabulário e frases das fontes de formas  interessantes.
'''

from exercise13_8_1 import get_pre_su
from exercise13_8_2 import random_txt

books = list()

with open('Books/pense_python/exercise13/file13-8-3_1.txt', 'r', encoding='utf-8') as file:
    for x in file:
        x = (x.replace('"', '').replace('(','').replace(')','').split())
        for y in x:
            books.append(y)

with open('Books/pense_python/exercise13/file13-8-3_2.txt', 'r', encoding='utf-8') as file:
    for x in file:
        x = (x.replace('"', '').replace('(','').replace(')','').split())
        for y in x:
            books.append(y)


if __name__ == "__main__":
    books = get_pre_su(books)
    random_txt(books)