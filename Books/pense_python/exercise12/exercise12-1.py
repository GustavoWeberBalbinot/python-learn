'''
Escreva uma função chamada most_frequent que receba uma string e exiba as letras em ordem decrescente de frequência. Encontre amostras de texto de vários idiomas diferentes e veja como a frequência das letras varia entre os idiomas. Compare seus resultados com as tabelas em http://en.wikipedia.org/wiki/Letter_frequencies.
'''

def most_frequent(word = str()):
    word = word.replace(' ', '')
    d = dict()
    for i in word:
        d[i] = d.get(i,0) + 1
    d = list_itens_dict(d)
    for x in sorted(d, reverse=True):
        print(f'{x}: [ ', end='')
        for sequence in d[x]:
            print(f'{sequence} ', end='')
        print(']')
    return d

def list_itens_dict(d):
    inverse = dict()
    for key in d:
        value = d[key]
        if value not in inverse:
            inverse[value] = [key]
        else:
            inverse[value].append(key)
    return inverse

most_frequent('brontosaurus')
