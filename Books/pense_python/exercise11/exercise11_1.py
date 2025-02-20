'''
Escreva uma função que leia as palavras em words.txt e guarde-as como chaves em um dicionário. Não importa quais são os valores. Então você pode usar o operador in como uma forma rápida de verificar se uma string está no dicionário.
'''

with open('Books/pense_python/exercise11/file.txt', 'r') as file:
    conteudo = file.read()
    itens = conteudo.lower().split(';')


def read_file(list_itens):
    d = dict()
    for x in (list_itens):
        d[x] = []
    return d

def search_iten(list_itens, value_item=''):
    if value_item in list_itens:
        return True
    else:
        return False

new_dict = read_file(itens)
item_to_search = 'listen'
print(search_iten(new_dict, item_to_search))